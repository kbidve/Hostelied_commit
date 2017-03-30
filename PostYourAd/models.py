from django.db import models
from _elementtree import parse
from UserAdministrator.models import UserInfo


class CotBasisRooms(models.Model):
    room_rent = models.IntegerField()
    address = models.CharField(max_length=200)
    user_id = models.ForeignKey(UserInfo , related_name='rooms' , default=1, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.address 

class FlatOnRent(models.Model):
    flat_type = models.CharField(max_length=100)
    furnishing_type = models.CharField(max_length=100)
    user_id = models.ForeignKey(UserInfo , related_name='flats' , default=1, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.flat_type +  " - " + self.furnishing_type