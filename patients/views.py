from django.shortcuts import render
from .models import Patient
from .serializers import PatientSerializer
from rest_framework import viewsets


# Create your views here.
class PatienViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer

    def get_queryset(self): 
    	return Patient.objects.filter(specialist=self.request.user)