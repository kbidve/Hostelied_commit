from rest_framework import serializers

from .models import Mess_Info, Thali_Details


class Mess_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mess_Info
        fields = '__all__'
        
class Thali_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thali_Details
        fields = '__all__'