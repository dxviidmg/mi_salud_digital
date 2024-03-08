from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient
from specialists.models import ConsultingRoom


class Consultation(models.Model):
    STATUS_CHOICES = ((0, "Sin confirmar"), (1, "Confirmado"), (2, "Cancelado"))

    specialist = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    consulting_room = models.ForeignKey(
        ConsultingRoom, on_delete=models.CASCADE
    )
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return "{} {} {}".format(self.specialist, self.patient, self.date_time)
