# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PostYourAd', '0021_auto_20170420_0210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat_furnishing_details',
            name='furnishing_details',
        ),
        migrations.RemoveField(
            model_name='flat_furnishing_details',
            name='furniture',
        ),
        migrations.RemoveField(
            model_name='flatonrent',
            name='flat_image',
        ),
        migrations.AddField(
            model_name='flat_furnishing_details',
            name='flat_image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='flat_furnishing_details',
            name='flat_image_details',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='flat_images', to='PostYourAd.FlatOnRent'),
        ),
    ]
