# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostYourFoodAd', '0003_auto_20170422_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='mess_info',
            name='mess_name',
            field=models.CharField(default='some string', max_length=100),
        ),
    ]
