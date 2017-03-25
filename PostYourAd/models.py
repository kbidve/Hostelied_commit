from django.db import models
from _elementtree import parse

class CotBasisRooms(models.Model):
    room_rent = models.IntegerField()
    address = models.CharField(max_length=200)
