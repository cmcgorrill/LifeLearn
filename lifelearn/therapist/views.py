from django.http import HttpResponse
from django.shortcuts import render

def testView(request):
	return render(request, "index.html")

def therapistlogin(request):
	return render(request, "therapist-login.html")
	
def dashboard(request):
	return render(request, "dashboard.html")


def calendar(request):
	return render(request, "calendar.html")

def addPatient(request):
	return render(request, "edit-patient.html")

def editPatient(request):
	return render(request, "edit-patient.html")

def addTask(request):
	return render(request, "edit-task.html")

def editTask(request):
	return render(request, "edit-task.html")

def patientInfo(request):
	return render(request, "patient-info.html")

def manageTasks(request):
	return render(request, "manage-tasks.html")


def patientDashboard(request):
	return render(request, "patient-dashboard.html")

def completeTask(request):
	return render(request, "complete-task.html")