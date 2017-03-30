from rest_framework import generics
from .models import UserInfo
from .serializers import UserSerializer
from rest_framework.views import APIView
from PostYourAd.models import CotBasisRooms
from PostYourAd.serializers import CotBasisRoomsSerializer
from rest_framework.response import Response


class UserList(generics.ListCreateAPIView):
    queryset=UserInfo.objects.all()
    serializer_class = UserSerializer

class UserDetais(generics.RetrieveUpdateDestroyAPIView):
    queryset=UserInfo.objects.all()
    serializer_class = UserSerializer
    
class UsersAdsList(APIView):
    def get(self, request , user_id ,format='json'):
        queryset= CotBasisRooms.objects.filter(user_id=user_id)
        serializer= CotBasisRoomsSerializer(queryset , many=True)
        return Response(serializer.data)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import UserSerializer
# from django.contrib.auth.models import User
# 
# class UserCreate(APIView):
#     """ 
#     Creates the user. 
#     """
# 
#     def post(self, request, format='json'):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)