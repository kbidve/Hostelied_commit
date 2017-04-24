# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from UserAdministrator.models import UserInfo

class Mess_Info(models.Model):
    mess_name = models.CharField(max_length=100, default = 'some string')
    mess_type  =models.CharField(max_length=100)
    veg_thali_prize_per_thali = models.IntegerField(default=0)
    veg_thali_prize_per_month_one_time = models.IntegerField(default=0)
    veg_thali_prize_per_month_both_time = models.IntegerField(default=0)
    nonveg_thali_prize_per_thali = models.IntegerField(default=0)
    nonveg_thali_prize_per_month_one_time = models.IntegerField(default=0)
    nonveg_thali_prize_per_month_both_time = models.IntegerField(default=0)
    address = models.CharField(max_length=200 , default = 'some string')
    user_id = models.ForeignKey(UserInfo , related_name='mess' , default=1, on_delete= models.CASCADE)
    description = models.CharField(max_length=500 , default = 'some string')
    location = models.PointField(null=True , blank = True)
    
class Thali_Details(models.Model):
    vegetable  = models.IntegerField(default=1)
    roti = models.IntegerField(default=1)
    dal = models.IntegerField(default=1)
    rice = models.IntegerField(default=1)
    salad = models.CharField(max_length=200 , default = 'some string')
    thali_details = models.ForeignKey(Mess_Info , on_delete=models.CASCADE , related_name='thali_details' , default=1)