# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import loader
from urllib.request import Request, urlopen
from io import StringIO
import json, requests
from home.models import User, Course
import itertools
from zeep import Client

# Courses url
COURSES_URL = "http://www.athenea-project.org/courses-microservice/api/course/all"
COURSES_TAG = "http://www.athenea-project.org/courses-microservice/api/course/tag"
ORGANIZATION_COURSES_URL = "http://www.athenea-project.org/courses_organizations-microservice/api/course_organizations/all"
CLIENT = Client("http://localhost:8080/comments/CommentResourceServiceImplPort?wsdl")
COURSES_PER_PAGE = 3

# Create your views here.



def index(request):
    page_number = request.session['page_number']
    if Course.objects.count() < (page_number*COURSES_PER_PAGE):
        download_courses()
    course_list = Course.objects.all()[((page_number-1)*COURSES_PER_PAGE):(page_number*COURSES_PER_PAGE)]
    print(course_list)
    context = {
            'course_list': course_list,
            'user': request.session['user.name'],
            'page_number': page_number,
            'page_prev': page_number-1,
            'page_next': page_number+1,
            'courses_size': Course.objects.count(),
            'max_allowed': page_number*COURSES_PER_PAGE

        }

    # Fetch organization courses and create a JSON
    req = Request(ORGANIZATION_COURSES_URL)
    req.add_header('accept','application/json')
    data = urlopen(req).read()
    dataDecoded = data.decode('utf8').replace("'", '"')

    return render(request, 'home.html', context)

def course_detail(request, course_id):
    course = Course.objects.get(course_id=course_id)
    comments = CLIENT.service.findCommentsForCourse("string")
    print(type(comments))
    comment_count=0
    if comments is not None:
        comment_count=len(comments)
    context = {
        'course':  course,
        'user': request.session['user.name'],
        'comments': comments,
        'comment_count': comment_count
    }
    return render(request, "course.html", context )

def user_detail(request, username):
    return HttpResponse("These are the details of the user %s." % username)

def search(request):
    tag = request.POST['search']
    print (tag)
    headers = {'accept': 'application/json','tag': tag}
    r = requests.get(COURSES_TAG, headers=headers)
        
    courses = r.json()
    course_search = []
    for c in courses:
        course_search.append(Course.objects.get(course_id=c['id']))
    print (courses)

    context = {
        'course_search': course_search,
        'user': request.session['user.name']
    }

    return render(request, 'search.html', context)

def index_page(request, page):
    request.session['page_number'] = page
    if Course.objects.count() < (page*COURSES_PER_PAGE):
        print("Downloading courses")
        download_courses()
    course_list = Course.objects.all()[((page-1)*COURSES_PER_PAGE):(page*COURSES_PER_PAGE)]
    print(course_list)
    context = {
            'course_list': course_list,
            'user': request.session['user.name'],
            'page_number': page,
            'page_prev': page-1,
            'page_next': page+1,
            'courses_size': Course.objects.count(),
            'max_allowed': page*COURSES_PER_PAGE

    }

    # Fetch organization courses and create a JSON
    req = Request(ORGANIZATION_COURSES_URL)
    req.add_header('accept','application/json')
    data = urlopen(req).read()
    dataDecoded = data.decode('utf8').replace("'", '"')

def map(request):
    #TODO: geoJSON con los cursos
    page_number = request.session['page_number']
    if Course.objects.count() < (page_number*COURSES_PER_PAGE):
        print("Downloading courses")
        download_courses()
    course_list = Course.objects.all()
    print(course_list)
    points = []

    for c in course_list:
        points.append('{"type": "Feature","geometry": {"type": "Point","coordinates": ['+ str(c.latitude) + ',' + str(c.longitude) + ']},"properties": {"title":"' + c.name + '","description":"' +  c.profesorEmail + '"}}')
    points = str(points)
    points = points.replace("'", "")
    context = {
        'courses': course_list,
        'points': points
    }

    return render(request, "map.html", context)
    
def download_courses():
    headers = {'accept': 'application/json'}
    r = requests.get(COURSES_URL, headers=headers)
    courses = r.json()
    print(courses)
    for c in courses:
        if not Course.objects.filter(course_id=c['id']):
            course = Course(course_id = c['id'],
                        name = c['name'],
                        description = c['description'],
                        latitude = c['latitude'],
                        longitude = c['longitude'],
                        profesorEmail =c['profesorEmail'],
                        price = c['price'],
                        likes = c['likes'])
            course.save()

def submit_comment(request):
    if request.method == 'POST':
        if request.POST['comment']:
                comments = CLIENT.service.insert(request.POST['course_id'],request.POST['user'],request.POST['comment'])
    url = "/course/"+request.POST['course_id']
    return redirect(url)


