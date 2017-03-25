from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CotBasisRoomsSerializer
from django.contrib.auth.models import User
from .models import CotBasisRooms

class CotBasisDetails(APIView):
    """ 
    Creates the Room Details. 
    """

    def post(self, request, format='json'):
        serializer = CotBasisRoomsSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def get(self, request, format='json'):
        data = CotBasisRooms.objects.all()
        serializer = CotBasisRoomsSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)