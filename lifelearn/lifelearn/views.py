from django.http import HttpResponse
from django.shortcuts import render

def testView(request):
	return render(request, "index.html")

def dashboard(request):
	return render(request, "dashboard.html")

def calendar(request):
	return render(request, "calendar.html")

def addPatient(request):
	return render(request, "add-patient.html")

def editTask(request):
	return render(request, "edit-task.html")

def patientInfo(request):
	return render(request, "patient-info.html")

def patientDashboard(request):
	return render(request, "patient-dashboard.html")