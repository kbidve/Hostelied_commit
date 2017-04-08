from django.db import models
from _elementtree import parse
from UserAdministrator.models import UserInfo


class Room_Amanities(models.Model):
    amenity = models.CharField(max_length = 20, blank=True)
    def __str__(self):
        return self.amenity
    
class CotBasisRooms(models.Model):
    room_rent_type = models.CharField(max_length = 100 , blank = True)
    room_rent = models.IntegerField()
    address = models.CharField(max_length=200)
    room_image = models.FileField(null = True , blank =True)
    user_id = models.ForeignKey(UserInfo , related_name='rooms' , default=1, on_delete= models.CASCADE)
    deposite = models.IntegerField(null = True)
    room_type = models.CharField(max_length = 100, blank=True)
    gender = models.CharField(max_length= 20 , blank= True)
    description = models.CharField(max_length = 500 , blank= True)
    amenities = models.ManyToManyField(Room_Amanities)
    def __str__(self):
        return self.address
    
class FlatOnRent(models.Model):
    flat_type = models.CharField(max_length=100)
    furnishing_type = models.CharField(max_length=100)
    flat_image = models.FileField(null = True , blank =True)
    user_id = models.ForeignKey(UserInfo , related_name='flats' , default=1, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.flat_type +  " - " + self.furnishing_type