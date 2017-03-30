from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CotBasisRoomsSerializer, FlatOnRentSerializer
from django.contrib.auth.models import User
from .models import CotBasisRooms, FlatOnRent
from rest_framework import generics


class CotBasisList(generics.ListCreateAPIView):
    queryset=CotBasisRooms.objects.all()
    serializer_class = CotBasisRoomsSerializer

class CotBasisDetais(generics.RetrieveUpdateDestroyAPIView):
    queryset=CotBasisRooms.objects.all()
    serializer_class = CotBasisRoomsSerializer

class FlatOnRentList(generics.ListCreateAPIView):
    queryset=FlatOnRent.objects.all()
    serializer_class = FlatOnRentSerializer

class FlatOnRentDetais(generics.RetrieveUpdateDestroyAPIView):
    queryset=FlatOnRent.objects.all()
    serializer_class = FlatOnRentSerializer
