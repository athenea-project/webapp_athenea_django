# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import Request, urlopen

# Create your views here.

# User url for login
user_url = "http://www.athenea-project.org/users-microservice/api/user/usernamePass"

def index(request):
    return render(request, 'login.html',)


def checkLogin(request):
    print(request)
    username = request.POST['username']
    print(username)
    #req = Request(user_url)
    #req.add_header('accept','application/json')
    #req.add_header('username',username)
    #req.add_header('password',password)
    #data = urlopen(req).read()
    #dataDecoded = data.decode('utf8').replace("'", '"')
    return HttpResponse('/login')