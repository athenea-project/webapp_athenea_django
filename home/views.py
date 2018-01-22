# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import Request, urlopen
from io import StringIO
import json, requests

# Courses url
courses_url = "http://www.athenea-project.org/courses-microservice/api/course/all"
organization_courses_url = "http://www.athenea-project.org/courses_organizations-microservice/api/course_organizations/all"

# Create your views here.



def index(request):
    # Fetch courses and create a JSON
    req = Request(courses_url)
    req.add_header('accept','application/json')
    data = urlopen(req).read()
    dataDecoded = data.decode('utf8').replace("'", '"')
    print(dataDecoded)

    # Fetch organization courses and create a JSON
    req = Request(organization_courses_url)
    req.add_header('accept','application/json')
    data = urlopen(req).read()
    dataDecoded = data.decode('utf8').replace("'", '"')
    print(dataDecoded)

    return render(request, 'home.html')


#def index(request):
#    return render(request, 'home.html',)

