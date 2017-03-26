from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CotBasisRoomsSerializer
from django.contrib.auth.models import User
from .models import CotBasisRooms
from rest_framework import generics


class CotBasisList(generics.ListCreateAPIView):
    queryset=CotBasisRooms.objects.all()
    serializer_class = CotBasisRoomsSerializer

class CotBasisDetais(generics.RetrieveUpdateDestroyAPIView):
    queryset=CotBasisRooms.objects.all()
    serializer_class = CotBasisRoomsSerializer


# class CotBasisDetails(APIView):
#     """ 
#     Creates the Room Details. 
#     """
# 
#     def post(self, request, format='json'):
#         serializer = CotBasisRoomsSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#     
#     
#     def get(self, request, ad_id=None, format='json'):
#         if(ad_id==None):
#             data = CotBasisRooms.objects.all()
#             serializer = CotBasisRoomsSerializer(data, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             data = CotBasisRooms.objects.get(pk=ad_id)
#             serializer = CotBasisRoomsSerializer(data)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         
