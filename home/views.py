# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import loader
from urllib.request import Request, urlopen
from io import StringIO
import json, requests
from home.models import User, Course
import itertools

# Courses url
COURSES_URL = "http://www.athenea-project.org/courses-microservice/api/course/all"
COURSES_TAG = "http://www.athenea-project.org/courses-microservice/api/course/tag"
ORGANIZATION_COURSES_URL = "http://www.athenea-project.org/courses_organizations-microservice/api/course_organizations/all"

# Create your views here.



def index(request):
    # Fetch courses and create a JSON
    # req = Request(COURSES_URL)
    # req.add_header('accept','application/json')
    # data = urlopen(req).read()
    # print(data.json())
    # dataDecoded = data.decode('utf8').replace("'", '"')
    # a = type(dataDecoded)
    # print(a)
    headers = {'accept': 'application/json'}
    r = requests.get(COURSES_URL, headers=headers)
    courses = r.json()
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
    course_list = Course.objects.all()
    print(course_list)
    context = {
        'course_list': course_list,
        'user': request.session['user.name']
    }

    # Fetch organization courses and create a JSON
    req = Request(ORGANIZATION_COURSES_URL)
    req.add_header('accept','application/json')
    data = urlopen(req).read()
    dataDecoded = data.decode('utf8').replace("'", '"')

    return render(request, 'home.html', context)

def course_detail(request, course_id):
    course = Course.objects.get(course_id=course_id)
    context = {
        'course':  course,
        'user': request.session['user.name']
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


#def index(request):
#    return render(request, 'home.html',)

