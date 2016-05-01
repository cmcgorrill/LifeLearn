from django.db import models

class Therapist(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	def getPatients(self):
		return Patient.objects.filter(therapist=self)