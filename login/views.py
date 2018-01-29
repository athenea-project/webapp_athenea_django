# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from urllib.request import Request, urlopen
from django.template import RequestContext
import json, urllib.parse, requests
from home.models import User


#TODO: Send the username and pass to the home view so it can use them
# User url for login
USER_URL = "http://www.athenea-project.org/users-microservice/api/user/usernamePass"
REGISTER_URL = "http://www.athenea-project.org/users-microservice/api/user/insert"


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
            results = requests.post(REGISTER_URL,  
              headers={'accept': 'application/json', 'content-type' : 'application/json'},
              data="{\"email\": \""+request.POST['emauil_us']+"\",  \"password\": \""+request.POST['pass_us']+"\",  \"name\": \""+request.POST['name_us']+"\",  \"username\": \""+request.POST['username_us']+"\",  \"phone_number\": "+request.POST['phone_us']+"}")
            if results == "<Response [200]>":
                return render(request, 'home.html', {'user': user})
            elif results == "<Response [403]>":
                #TODO: download all the usernames of the database and check live
                headers = {'accept': 'application/json'}
                r = requests.get(COURSES_URL, headers=headers)
                courses = r.json()
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
            # req = Request(USER_URL)
            # req.add_header('accept', 'application/json')
            # req.add_header('username' ,username)
            # req.add_header('password' ,password)
            # data = urlopen(req).read()
            headers = {'accept': 'application/json', 'username': username, 'password':password}
            r = requests.get(USER_URL, headers=headers)
            user = r.json()
            print(user)
            if not user:
                errors.append('Enter a valid username/password')
            else:    
                print("Generarting new user")
                u = User(phone_number= user['phone_number'],
                    email= user['email'],
                    name= user['name'], 
                    password= user['password'], 
                    username= user['username']                
                )
                print(u)
                return redirect('/home', {'user': u})
        return render(request, 'login.html', {'errors': errors})
    return HttpResponse('/login')
