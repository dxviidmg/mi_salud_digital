from rest_framework import serializers
from .models import ConsultingRoom
from django.contrib.auth.models import User


class ConsultingRoomSerializer(serializers.ModelSerializer):    
    full_address = serializers.SerializerMethodField()

    def get_full_address(self, obj):
        return obj.get_full_address()


    class Meta:
        model = ConsultingRoom
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        exclude = ['password']