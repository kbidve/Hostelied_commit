from django.contrib.gis.db import models
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
    location = models.PointField(null=True , blank = True)
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
    flat_rent = models.IntegerField(default=0)
    deposit = models.IntegerField(default=0 , null = True)
    address = models.CharField(max_length=200 , default = 'some string')
    no_of_persons_allowed = models.IntegerField(default=1)
    description = models.CharField(max_length=500 , default = 'some string')
    maintainance_charge = models.IntegerField(default=0 , null = True)
    no_of_bathrooms = models.IntegerField(default=1)
    no_of_balconies = models.IntegerField(default=0)
    floor_no = models.IntegerField(default=1)
    total_floor = models.IntegerField(default=1)
    lift = models.BooleanField(default=False)
    location = models.PointField(null=True , blank = True)
    
    
    def __str__(self):
        return self.flat_type +  " - " + self.furnishing_type
    
class Flat_Furnishing_Details(models.Model):
    furniture = models.CharField(max_length = 20, blank=True)
    furnishing_details = models.ForeignKey(FlatOnRent , on_delete=models.CASCADE , related_name='furnitures')
    def __str__(self):
        return self.furniture