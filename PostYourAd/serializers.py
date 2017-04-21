from django.contrib.auth.models import User
from rest_framework import serializers

from .models import CotBasisRooms, FlatOnRent, Room_Amanities , Flat_Images_Details

class Room_AmanitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room_Amanities
        fields = ('amenity' ,)
        
class Flat_Images_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat_Images_Details
        fields = ('flat_image' ,)
        
        
class CotBasisRoomsSerializer(serializers.ModelSerializer):
    amenities= Room_AmanitiesSerializer(read_only=True, many=True)
    distance = serializers.DecimalField(source = 'distance.mi' , max_digits= 10 , decimal_places= 2, required = False ,
                                        read_only = True)
    class Meta:
        model = CotBasisRooms
        fields= '__all__'
        extra_field = ('amenities',)
        read_only_fields = ('location',)
#         fields = ('id', 'room_rent', 'address', 'user_id' , 'room_image' , 'amenities' , 'room_rent_type',
#                   'deposite' , 'room_type' , 'gender' , 'description', )
        
class FlatOnRentSerializer(serializers.ModelSerializer):
    flat_images = Flat_Images_DetailsSerializer(many=True)
    class Meta:
        model = FlatOnRent
        fields = '__all__'
        extra_field = ('flat_images',)
        #fields = ('id', 'flat_type' , 'furnishing_type', 'user_id' , 'flat_image')
        
