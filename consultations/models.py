from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient

class Consultation(models.Model):
	specialist = models.ForeignKey(User, on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	date_time = models.DateTimeField()

	def __str__(self) -> str:
			return '{} {} {}'.format(self.specialist, self.patient, self.date_time)