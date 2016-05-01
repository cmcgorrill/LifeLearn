from django.db import models

class Task(models.Model):
	name = models.CharField(max_length=100)
	info = models.CharField(max_length=500)

	# video url
	video = models.CharField(max_length=100)

	
	cards = models.CharField(max_length=200)

class Card(models.Model):
	text = models.CharField(max_length=100)

	# image url
	image = models.CharField(max_length=100)