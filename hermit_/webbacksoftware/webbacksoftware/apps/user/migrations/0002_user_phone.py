# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-06-17 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=11, unique=True, verbose_name='phonenum'),
        ),
    ]
