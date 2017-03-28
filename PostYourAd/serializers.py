from django.contrib.auth.models import User
from rest_framework import serializers

from .models import CotBasisRooms


class CotBasisRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotBasisRooms
        fields = ('id', 'room_rent', 'address', 'user_id')