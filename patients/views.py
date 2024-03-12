from django.shortcuts import render
from .models import Patient
from .serializers import PatientSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


# Create your views here.
class PatienViewSet(viewsets.ModelViewSet):
	serializer_class = PatientSerializer

	def get_queryset(self): 
		return Patient.objects.filter(specialist=self.request.user)
	
	def create(self, request, *args, **kwargs):
		# Assuming you pass token in the request headers
		token = request.headers.get('Authorization').split(' ')[1]
		specialist = User.objects.get(auth_token__key=token)  # Assuming Author has a OneToOneField to User
		request.data['specialist'] = specialist.pk
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
		