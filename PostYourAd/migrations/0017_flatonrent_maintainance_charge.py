# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostYourAd', '0016_flatonrent_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatonrent',
            name='maintainance_charge',
            field=models.IntegerField(default=0, null=True),
        ),
    ]