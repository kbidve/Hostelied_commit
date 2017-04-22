from django.contrib.auth.models import User
from rest_framework import serializers

from .models import CotBasisRooms, FlatOnRent, Room_Amanities , Flat_Images_Details, Flat_Furnishing_Details
from UserAdministrator.serializers import UserSerializer

class Room_AmanitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room_Amanities
        fields = ('amenity' ,)
        
class Flat_Images_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat_Images_Details
        fields = ('flat_image' ,)
        
        
class Flat_Furnishing_Details(serializers.ModelSerializer):
    class Meta:
        model = Flat_Furnishing_Details
        fields = ('furniture',)
        
class CotBasisRoomsSerializer(serializers.ModelSerializer):
    amenities= Room_AmanitiesSerializer(many=True, read_only=True)
    distance = serializers.DecimalField(source = 'distance.mi' , max_digits= 10 , decimal_places= 2, required = False ,
                                        read_only = True)
    user = UserSerializer(source = 'user_id')
    class Meta:
        model = CotBasisRooms
        fields= '__all__'
        extra_field = ('amenities',)
        read_only_fields = ('location', 'user')

        
class FlatOnRentSerializer(serializers.ModelSerializer):
    flat_images = Flat_Images_DetailsSerializer(many=True, read_only=True)
    furnishing_details = Flat_Furnishing_Details(many=True, read_only=True)
    user = UserSerializer(source = 'user_id')
    distance = serializers.DecimalField(source = 'distance.mi' , max_digits= 10 , decimal_places= 2, required = False ,
                                        read_only = True)
    class Meta:
        model = FlatOnRent
        fields = '__all__'
        extra_field = ('flat_images','furnishing_details', 'user')
        read_only_fields = ('location',)

        
