# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-01-17 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32, unique=True)),
                ('phonenum', models.CharField(max_length=16, unique=True)),
                ('sex', models.BooleanField(default=True)),
                ('avatar', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=128)),
                ('birth_year', models.IntegerField(default=2000)),
                ('birth_month', models.IntegerField(default=1)),
                ('birth_day', models.IntegerField(default=1)),
            ],
        ),
    ]