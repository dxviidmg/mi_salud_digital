from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):    
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return obj.get_full_name()


    class Meta:
        model = Patient
        fields = "__all__"