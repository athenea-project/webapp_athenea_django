from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    path(r'/<int:page>', views.index_page),


]