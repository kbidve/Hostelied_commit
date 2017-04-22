from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import UserInfo

class UserSerializer(serializers.ModelSerializer):
    email_id = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=UserInfo.objects.all())]
            )
    

    class Meta:
        model = UserInfo
        fields = ('id', 'name', 'contact_no', 'email_id')