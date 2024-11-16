from .models import Consultation
from rest_framework import viewsets
from .serializers import ConsultationSerializer, ConsultationCreatedSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from patients.models import Patient
from patients.serializers import PatientSerializer
from datetime import datetime
from specialists.models import Availability
from specialists.serializers import ConsultingRoomSerializer
from django.shortcuts import get_object_or_404


class ConsultationViewSet(viewsets.ModelViewSet):
#	serializer_class = ConsultationSerializer

	def get_serializer_class(self):
		if self.request.method == 'POST':
			return ConsultationCreatedSerializer
		return ConsultationSerializer
	def get_queryset(self): 
		return Consultation.objects.filter(specialist=self.request.user)
	
	
	def create(self, request, *args, **kwargs):
		token = request.headers.get('Authorization').split(' ')[1]
		specialist = User.objects.get(auth_token__key=token)  # Assuming Author has a OneToOneField to User

		date_time = request.data.get('date_time')
		date_time_obj = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S%z')
		if Consultation.objects.filter(date_time=date_time_obj, specialist=specialist).exists():
			return Response({"error": "Ya existe una consulta para esta fecha y hora"}, status=status.HTTP_400_BAD_REQUEST)

		request.data['specialist'] = specialist.pk
#		Patient.objects.
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
	