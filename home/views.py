# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import urllib3, json, requests

# Courses url
courses_url = "http://www.athenea-project.org/courses-microservice/api/course/all"

# Create your views here.

def index(request):
  payload = {'accept':'application/json'}
  data = requests.get('http://www.athenea-project.org/courses-microservice/api/course/all', params=payload)  
  
  print(data)
  return HttpResponse("Hello, world. You're at the polls index.")
