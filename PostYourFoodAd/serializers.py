from rest_framework import serializers

from .models import Mess_Info, Thali_Details
from UserAdministrator.serializers import UserSerializer


class Thali_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thali_Details
        fields = '__all__'
        
class Mess_InfoSerializer(serializers.ModelSerializer):
    thali_details = Thali_DetailsSerializer(many=True, read_only=True)
    user = UserSerializer(source = 'user_id', read_only = True)
    distance = serializers.DecimalField(source = 'distance.mi' , max_digits= 10 , decimal_places= 2, required = False ,
                                        read_only = True)
    class Meta:
        model = Mess_Info
        fields = '__all__'
        read_only_fields = ('location', 'user')
        extra_field = ('thali_details',)
        
