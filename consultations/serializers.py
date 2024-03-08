from rest_framework import serializers
from .models import Consultation
from datetime import timedelta
from patients.serializers import PatientSerializer
from specialists.serializers import ConsultingRoomSerializer

class ConsultationSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    consulting_room = ConsultingRoomSerializer()
    
    date_time_end = serializers.SerializerMethodField()

    def get_date_time_end(self, obj):
        return obj.date_time + timedelta(minutes=obj.specialist.profile.appointment_duration)
    
    class Meta:
        model = Consultation
        fields = "__all__"