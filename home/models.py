# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 20)
    name = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20)
    phone_number = models.IntegerField()


class Course(models.Model):
    id = models.CharField(max_length = 10)
    name = models.CharField(max_length = 20)
    description = models.TextField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    profesorEmail = models.CharField(max_length = 45)
    price = models.IntegerField()
    likes = models.IntegerField()

class Organization_Course(models.Model):
    

#class Tags(models.Model):

# "tags": [
#  "string"