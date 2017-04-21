# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 01:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PostYourAd', '0019_flatonrent_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat_Furnishing_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('furniture', models.CharField(blank=True, max_length=20)),
                ('furnishing_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PostYourAd.FlatOnRent')),
            ],
        ),
    ]