from django.contrib.auth.models import User

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import ConsultingRoom
from django.core import serializers 

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)
        consulting_rooms = ConsultingRoom.objects.filter(specialist=user)

        serialized_rooms = []
        for room in consulting_rooms:
            serialized_rooms.append({
                'id': room.pk,
                'full_address': room.get_full_address(),
                # Add other fields as needed
            })
        
        print('consulting_rooms', consulting_rooms)
        return Response({
            'user_id': user.pk,
            'token': token.key,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'full_name': user.get_full_name(),
            'availability_time_range': user.get_availability_time_range(),
            'consulting_rooms': serialized_rooms
        })