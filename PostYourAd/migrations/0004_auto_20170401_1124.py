# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-01 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostYourAd', '0003_auto_20170331_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotbasisrooms',
            name='room_image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='flatonrent',
            name='flat_image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]