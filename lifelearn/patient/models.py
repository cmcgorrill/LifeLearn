from django.db import models
from therapist.models import Therapist

class Patient(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	info = models.CharField(max_length=500)
	therapist = models.ForeignKey(Therapist)