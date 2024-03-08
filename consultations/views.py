from .models import Consultation
from rest_framework import viewsets
from .serializers import ConsultationSerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    serializer_class = ConsultationSerializer

    def get_queryset(self): 
        return Consultation.objects.filter(specialist=self.request.user)