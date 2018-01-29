# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from urllib.request import Request, urlopen
from django.template import RequestContext
import json, urllib.parse, requests


#TODO: Send the username and pass to the home view so it can use them
# User url for login
user_url = "http://www.athenea-project.org/users-microservice/api/user/usernamePass"
register_url = "http://www.athenea-project.org/users-microservice/api/user/insert"


def index(request):
    return render(request, 'login.html',)

def register(request):
    errors = []
    if request.method == 'POST':
        if not request.POST['emauil_us']:
            errors.append('Enter an email.')
        if not request.POST['pass_us']:
            errors.append('Enter a password')
        if not request.POST['name_us']:
            errors.append('Enter a name')
        if not request.POST['username_us']:
            errors.append('Enter an username')
        if not request.POST['phone_us']:
            errors.append('Enter a phone number')
        if not errors:
            results = requests.post(register_url,  
              headers={'accept': 'application/json', 'content-type' : 'application/json'},
              data="{\"email\": \""+request.POST['emauil_us']+"\",  \"password\": \""+request.POST['pass_us']+"\",  \"name\": \""+request.POST['name_us']+"\",  \"username\": \""+request.POST['username_us']+"\",  \"phone_number\": "+request.POST['phone_us']+"}")
            print(results)
            if results == "<Response [200]>":
                return HttpResponseRedirect('/home')
            elif results == "<Response [403]>":
                #TODO: download all the usernames of the database and check live
                #TODO: Check phone number
                errors.append('That username was already taken')
                return render(request, 'login.html', {'errors': errors})        
        return render(request, 'login.html', {'errors': errors})

def checkLogin(request):
    errors = []
    if request.method == 'POST':
        if not request.POST['username_us']:
            errors.append('Enter an username.')
        if not request.POST['pass_us']:
            errors.append('Enter a password')
        if not errors:
            username = request.POST['username_us']
            password = request.POST['pass_us']
            req = Request(user_url)
            req.add_header('accept','application/json')
            req.add_header('username',username)
            req.add_header('password',password)
            data = urlopen(req).read()
            print(data)
            if data == b'':
                errors.append('Enter a valid username/password')
            else:    
                dataDecoded = data.decode('utf8').replace("'", '"')
                print(dataDecoded)
                return HttpResponseRedirect('/home')
        return render(request, 'login.html', {'errors': errors})
    return HttpResponse('/login')