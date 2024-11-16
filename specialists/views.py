from django.contrib.auth.models import User

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import ConsultingRoom, Availability
from django.core import serializers 
from datetime import datetime, timedelta, date, time
from dateutil.relativedelta import relativedelta




class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)
        consulting_rooms = ConsultingRoom.objects.filter(specialist=user)
        availabilities = Availability.objects.filter(specialist=user)
        
        serialized_rooms = []
        for room in consulting_rooms:
            serialized_rooms.append({
                'id': room.pk,
                'full_address': room.get_full_address(),
                # Add other fields as needed
            })
        
        serialized_availabilities = []
        for availability in availabilities:
            my_date = date.today() - relativedelta(months=12)
            print(my_date)
            dt = datetime.combine(my_date, availability.start_time) - timedelta(minutes=15)
            dt1 = datetime.combine(my_date, availability.start_time)
            dt2 = datetime.combine(my_date, availability.end_time) + timedelta(minutes=15)
            dt3 = datetime.combine(my_date, availability.end_time)
            serialized_availabilities.extend(({
                'id': 1,
                'title': 'Entrada',
                'start_time': dt,
                'end_time': dt1, 
                'day': availability.day,
                'consulting_room': availability.consulting_room.get_full_address()
            },
            {
                'id': 2,
                'start_time': dt2,
                'end_time': dt3,
                'day': availability.day,
                'title': 'Salida',
                'consulting_room': availability.consulting_room.get_full_address()
            }
            ))

        print('consulting_rooms', consulting_rooms)
        return Response({
            'user_id': user.pk,
            'token': token.key,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'full_name': user.get_full_name(),
            'availability_time_range': user.get_availability_time_range(),
            'consulting_rooms': serialized_rooms,
            'availabilities': serialized_availabilities
        })