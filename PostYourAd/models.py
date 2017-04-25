from django.contrib.gis.db import models
from _elementtree import parse
from UserAdministrator.models import UserInfo


class Room_Amanities(models.Model):
    amenity = models.CharField(max_length = 20, blank=True)
    def __str__(self):
        return self.amenity
    
class CotBasisRooms(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
         )
    ROOM_RENT_TYPE_CHOICES = (
        ('Y', 'Yearly'),
        ('S', 'SemisterWise'),
        ('M', 'Monthly'),
        )
    ROOM_TYPE_CHOICES = (
        ('ONE' , 'Single Room'),
        ('TWO','Sharing With Another Student'),
        ('THREE','Sharing With Other Two'),
        ('FOUR', 'Sharing With Other Three'),
        )
    room_rent_type = models.CharField(max_length = 100 , blank = True, choices= ROOM_RENT_TYPE_CHOICES)
    room_rent = models.IntegerField()
    address = models.CharField(max_length=200)
    room_image = models.FileField(null = True , blank =True)
    user_id = models.ForeignKey(UserInfo , related_name='rooms' , default=1, on_delete= models.CASCADE)
    deposite = models.IntegerField(null = True)
    location = models.PointField(null=True , blank = True)
    room_type = models.CharField(max_length = 100, blank=True, choices= ROOM_TYPE_CHOICES)
    gender = models.CharField(max_length= 20 , blank= True, choices= GENDER_CHOICES)
    description = models.CharField(max_length = 500 , blank= True)
    amenities = models.ManyToManyField(Room_Amanities, blank= True)
    def __str__(self):
        return self.address
    
class Flat_Furnishing_Details(models.Model):
    furniture = models.CharField(max_length = 20, blank=True)
    def __str__(self):
        return self.furniture
    
class FlatOnRent(models.Model):
    FLAT_TYPE = (
        ('HallKitchen', 'HK'),
        ('RoomKitchen', 'RK'),
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        )
    FURNISHING_TYPE = (
        ('U', 'UNFURNISHED'),
        ('S','SEMI_FURNISHED'),
        ('F','FULLY_FURNISHED'),
        )
    flat_type = models.CharField(max_length=100, choices = FLAT_TYPE)
    furnishing_type = models.CharField(max_length=100, choices = FURNISHING_TYPE)
    furnishing_details = models.ManyToManyField(Flat_Furnishing_Details, blank= True)
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
    
class Flat_Images_Details(models.Model):
    flat_image = models.FileField(null = True , blank =True)
    flat_image_details = models.ForeignKey(FlatOnRent , on_delete=models.CASCADE , related_name='flat_images' , default=1)
