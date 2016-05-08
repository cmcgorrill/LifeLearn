from django.http import HttpResponse
from django.shortcuts import render
from patient.models import Patient

def testView(request):
	return render(request, "index.html")

def therapistlogin(request):
	return render(request, "therapist-login.html")
	
def dashboard(request):
	response = {}

	response["patients"] = Patient.objects.all()

	return render(request, "dashboard.html", response)


def calendar(request):
	return render(request, "calendar.html")

def addPatient(request):
	response = {}

	if(request.method == "POST"):
		try:
			# TODO: validate fields

			# Add patient to the database
			p = Patient()
			p.first_name = request.POST["patient-name"]
			p.last_name = request.POST["patient-last-name"]
			p.info = request.POST["patient-info"]
			p.save()

			response["success"] = "Patient was added sucessfully."

		# Will be raised if one of the POST fields is missing
		except KeyError: 
			response["error"] = "Check to make sure that each field is filled out completely."
		except Exception as e:
			response["error"] = "An error occured on our end. Try reloading the page and submitting again."
			print(e)

	return render(request, "add-patient.html", response)

def editPatient(request):
	return render(request, "edit-patient.html")

def addTask(request):
	return render(request, "edit-task.html")

def editTask(request):
	return render(request, "edit-task.html")

def patientInfo(request, id):
	return render(request, "patient-info.html")

def manageTasks(request):
	return render(request, "manage-tasks.html")


def patientDashboard(request):
	return render(request, "patient-dashboard.html")

def completeTask(request):
	return render(request, "complete-task.html")