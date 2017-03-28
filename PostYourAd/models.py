from django.db import models
from _elementtree import parse
from UserAdministrator.models import UserInfo

class CotBasisRooms(models.Model):
    room_rent = models.IntegerField()
    address = models.CharField(max_length=200)
    user_id = models.ForeignKey(UserInfo , default=1)
