"""lifelearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^login', views.therapistlogin, name='login'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^calendar', views.calendar, name='calendar'),

    url(r'^patient/add$', views.addPatient, name='addPatient'),
    url(r'^patient/(?P<id>[0-9]+)$', views.patientInfo, name='patientInfo'),
    url(r'^patient/(?P<id>[0-9]+)/edit$', views.editPatient, name='editPatient'),

    url(r'^task/add$', views.editTask, name='editTask'),
    url(r'^task/(?P<id>[0-9]+)/edit$', views.editTask, name='editTask'),
    url(r'^task/manage$', views.manageTasks, name='manageTasks'),
]