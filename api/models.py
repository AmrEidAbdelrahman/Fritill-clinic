from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Appointment(models.Model):
	admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')
	client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client')
	date = models.DateTimeField()
	create_time = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)
	finished = models.BooleanField(default=False)
	missed = models.BooleanField(default=False)
	cancel = models.BooleanField(default=False)


class RescheduleRequest(models.Model):
	appointment = models.ForeignKey("Appointment", on_delete=models.CASCADE)
	to = models.DateTimeField()
	approved = models.BooleanField(default=False)
	refuased = models.BooleanField(default=False)
	create_time = models.DateTimeField(auto_now_add=True)
