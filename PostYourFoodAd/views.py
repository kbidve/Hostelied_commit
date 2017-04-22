from .models import Mess_Info
from .serializers import Mess_InfoSerializer
from rest_framework import generics
import  geocoder
from django.contrib.gis.geos.geometry import GEOSGeometry
from django.contrib.gis.db.models.functions import Distance


class MessList(generics.ListCreateAPIView):
    queryset=Mess_Info.objects.all()
    serializer_class = Mess_InfoSerializer
    
    def perform_create(self, serializer):
        address = serializer.initial_data['address']
        g= geocoder.google(address)
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        pnt = 'POINT(' + str(latitude) + ' ' + str(longitude) +  ')'
        serializer.save(location=pnt)
        
        
    def get_queryset(self):
        qs  = Mess_Info.objects.all()
        latitude = self.request.query_params.get('lat' , None)
        longitude = self.request.query_params.get('lng' , None)
         
        if latitude and longitude :
            pnt = Mess_Info('POINT(' + str(latitude) + ' ' + str(longitude) +  ')' , srid = 4326)
            print "Latitude = " + latitude
            print "Longitude = " + longitude
            qs = qs.annotate(distance = Distance('location', pnt)).order_by('distance')
        return qs


class MessDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Mess_Info.objects.all()
    serializer_class = Mess_InfoSerializer
    
    def perform_create(self, serializer):
        address = serializer.initial_data['address']
        g= geocoder.google(address)
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        pnt = 'POINT(' + str(latitude) + ' ' + str(longitude) +  ')'
        serializer.save(location=pnt)