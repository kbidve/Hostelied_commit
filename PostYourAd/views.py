from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CotBasisRoomsSerializer, FlatOnRentSerializer
from django.contrib.auth.models import User
from .models import CotBasisRooms, FlatOnRent
from rest_framework import generics
import  geocoder
from django.contrib.gis.geos.geometry import GEOSGeometry
from django.contrib.gis.db.models.functions import Distance


class CotBasisList(generics.ListCreateAPIView):
    queryset=CotBasisRooms.objects.all()
    serializer_class = CotBasisRoomsSerializer
    
    def perform_create(self, serializer):
        address = serializer.initial_data['address']
        g= geocoder.google(address)
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        pnt = 'POINT(' + str(latitude) + ' ' + str(longitude) +  ')'
        serializer.save(location=pnt)
        
        
    def get_queryset(self):
        qs  = CotBasisRooms.objects.all()
        latitude = self.request.query_params.get('lat' , None)
        longitude = self.request.query_params.get('lng' , None)
         
        if latitude and longitude :
            pnt = GEOSGeometry('POINT(' + str(latitude) + ' ' + str(longitude) +  ')' , srid = 4326)
            print "Latitude = " + latitude
            print "Longitude = " + longitude
            qs = qs.annotate(distance = Distance('location', pnt)).order_by('distance')
        return qs

class CotBasisDetais(generics.RetrieveUpdateDestroyAPIView):
    queryset=CotBasisRooms.objects.all()
    serializer_class = CotBasisRoomsSerializer
    
    def perform_create(self, serializer):
        address = serializer.initial_data['address']
        g= geocoder.google(address)
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        pnt = 'POINT(' + str(latitude) + ' ' + str(longitude) +  ')'
        serializer.save(location=pnt)

class FlatOnRentList(generics.ListCreateAPIView):
    queryset=FlatOnRent.objects.all()
    serializer_class = FlatOnRentSerializer
    
    def perform_create(self, serializer):
        address = serializer.initial_data['address']
        g= geocoder.google(address)
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        pnt = 'POINT(' + str(latitude) + ' ' + str(longitude) +  ')'
        serializer.save(location=pnt)
        
        
    def get_queryset(self):
        qs  = FlatOnRent.objects.all()
        latitude = self.request.query_params.get('lat' , None)
        longitude = self.request.query_params.get('lng' , None)
         
        if latitude and longitude :
            pnt = GEOSGeometry('POINT(' + str(latitude) + ' ' + str(longitude) +  ')' , srid = 4326)
            print "Latitude = " + latitude
            print "Longitude = " + longitude
            qs = qs.annotate(distance = Distance('location', pnt)).order_by('distance')
        return qs

class FlatOnRentDetais(generics.RetrieveUpdateDestroyAPIView):
    queryset=FlatOnRent.objects.all()
    serializer_class = FlatOnRentSerializer
