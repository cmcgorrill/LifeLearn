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
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.testView),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^calendar', views.calendar, name='calendar'),
    url(r'^add-patient', views.addPatient, name='addPatient'),
    url(r'^edit-patient', views.editPatient, name='editPatient'),
    url(r'^add-task', views.editTask, name='editTask'),
    url(r'^edit-task', views.editTask, name='editTask'),
    url(r'^patient-info', views.patientInfo, name='patientInfo'),
    url(r'^manage-tasks', views.manageTasks, name='manageTasks'),
    

    url(r'^patient-dashboard', views.patientDashboard, name='patientDashboard'),
    url(r'^complete-task', views.completeTask, name='completeTask'),
]
