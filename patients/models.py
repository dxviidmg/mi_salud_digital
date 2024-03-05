from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
	specialist = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	second_last_name = models.CharField(max_length=30)

	def get_full_name(self):
			return '{} {} {}'.format(self.first_name, self.last_name, self.second_last_name)
	
	def __str__(self):
		return self.get_full_name()
	