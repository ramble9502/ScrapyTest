# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kormovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('actor1', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
