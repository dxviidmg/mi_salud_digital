from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max, Min


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	appointment_duration = models.PositiveSmallIntegerField(verbose_name="Appointment Duration (In minutes)")

	def __str__(self) -> str:
		return 'Profile of {}'.format(self.user.get_full_name())
	
class ConsultingRoom(models.Model):
	specialist = models.ForeignKey(User, on_delete=models.CASCADE)
	street_name = models.CharField(max_length=50)
	street_number = models.CharField(max_length=50)
	neighborhood = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	zip_code = models.IntegerField()

	def get_full_address(self):
		return ', '.join([self.street_name + " " + self.street_number, self.neighborhood, self.city, self.state, str(self.zip_code)])
	

	def __str__(self) -> str:
		return self.get_full_address()
	


class Availability(models.Model):
	DAY_CHOICES = [
		('Monday', 'Monday'),
		('Tuesday', 'Tuesday'),
		('Wednesday', 'Wednesday'),
		('Thursday', 'Thursday'),
		('Friday', 'Friday'),
		('Saturday', 'Saturday'),
		('Sunday', 'Sunday'),
	]
		
	specialist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='availabilities')
	consulting_room = models.ForeignKey(ConsultingRoom, on_delete=models.CASCADE)
	start_time = models.TimeField()
	end_time = models.TimeField()
	day = models.CharField(max_length=10, choices=DAY_CHOICES)

	def __str__(self) -> str:
		return '{} from {} to {}'.format(self.day, self.start_time, self.end_time)
	


def get_availability_time_range(self):
	availabilities = self.availabilities.all()
	return availabilities.aggregate(start_time=Min('start_time'), end_time=Max('end_time'))


User.add_to_class("get_availability_time_range",get_availability_time_range)