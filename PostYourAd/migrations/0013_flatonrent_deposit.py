# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostYourAd', '0012_flatonrent_flat_rent'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatonrent',
            name='deposit',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
