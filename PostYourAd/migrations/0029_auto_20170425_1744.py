# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostYourAd', '0028_auto_20170425_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatonrent',
            name='furnishing_type',
            field=models.CharField(choices=[(b'U', b'UNFURNISHED'), (b'S', b'SEMI_FURNISHED'), (b'F', b'FULLY_FURNISHED')], max_length=100),
        ),
    ]
