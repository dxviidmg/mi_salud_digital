from rest_framework import serializers
from .models import ConsultingRoom

class ConsultingRoomSerializer(serializers.ModelSerializer):    
    full_address = serializers.SerializerMethodField()

    def get_full_address(self, obj):
        return obj.get_full_address()


    class Meta:
        model = ConsultingRoom
        fields = "__all__"