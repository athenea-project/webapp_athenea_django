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

    def __str__(self):
        return self.username


class Course(models.Model):
    course_id = models.CharField(max_length = 10)
    name = models.CharField(max_length = 20)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    profesorEmail = models.CharField(max_length = 45)
    price = models.IntegerField()
    likes = models.IntegerField()

    def __str__(self):
        return self.name

#class Organization_Course(models.Model):

