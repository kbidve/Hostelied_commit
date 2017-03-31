from rest_framework import generics
from .models import UserInfo
from .serializers import UserSerializer
from rest_framework.views import APIView
from PostYourAd.models import CotBasisRooms, FlatOnRent
from PostYourAd.serializers import CotBasisRoomsSerializer, FlatOnRentSerializer
from rest_framework.response import Response
from rest_framework.status import  HTTP_201_CREATED


class UserList(generics.ListCreateAPIView):
    queryset=UserInfo.objects.all()
    serializer_class = UserSerializer

class UserDetais(generics.RetrieveUpdateDestroyAPIView):
    queryset=UserInfo.objects.all()
    serializer_class = UserSerializer
    
class UsersAdsList(APIView):
    def get(self, request , user_id ,format='json'):
        queryset= CotBasisRooms.objects.filter(user_id=user_id)
        querysetflat = FlatOnRent.objects.filter(user_id=user_id)
        serializer= CotBasisRoomsSerializer(queryset , many=True)
        serializerflat = FlatOnRentSerializer(querysetflat ,many=True)
        return Response({
            'rooms' : serializer.data ,
            'flats' : serializerflat.data
            })


class UsersRoomAdsList(APIView):
    def get(self, request , user_id ,format='json'):
        queryset= CotBasisRooms.objects.filter(user_id=user_id)
        serializer= CotBasisRoomsSerializer(queryset , many=True)
        return Response({
            'rooms' : serializer.data 
            })
    def post(self , request, user_id  ,format='json'):
        serializer = CotBasisRoomsSerializer(data=request.data)
        if serializer.is_valid():
            room =serializer.save()
            if room:
                return Response(serializer.data, status=HTTP_201_CREATED)
            
class UsersFlatAdsList(APIView):
    def get(self, request , user_id ,format='json'):
        queryset= FlatOnRent.objects.filter(user_id=user_id)
        serializer= FlatOnRentSerializer(queryset ,many=True)
        return Response({
            'flats' : serializer.data 
            })
    
    def post(self , request, user_id  ,format='json'):
        serializer = FlatOnRentSerializer(data=request.data)
        if serializer.is_valid():
            flat =serializer.save()
            if flat:
                return Response(serializer.data, status=HTTP_201_CREATED)
        

class UsersRoomAdWithId(APIView):
    def get(self, request , user_id , ad_id ,format='json'):
        queryset= CotBasisRooms.objects.get(user_id=user_id)
        serializer= FlatOnRentSerializer(queryset ,many=True)
        return Response({
            'rooms' : serializer.data 
            })

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