"""webapp_athenea_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
import home

urlpatterns = [
    url(r'', include('login.urls')),
    url(r'^home', include('home.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^admin/', admin.site.urls),
    path('course/<str:course_id>', home.views.course_detail),
    path('user/<str:username>', home.views.user_detail),
    path('map', home.views.map),
    url('course/submit/comment', home.views.submit_comment),
    path('search', home.views.search)
]


