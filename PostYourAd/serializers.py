from django.contrib.auth.models import User
from rest_framework import serializers

from .models import CotBasisRooms, FlatOnRent


class CotBasisRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotBasisRooms
        fields = ('id', 'room_rent', 'address', 'user_id')
        
class FlatOnRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlatOnRent
        fields = ('id', 'flat_type' , 'furnishing_type', 'user_id')
        