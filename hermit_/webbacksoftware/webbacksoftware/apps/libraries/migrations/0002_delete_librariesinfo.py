# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-08 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LibrariesInfo',
        ),
    ]
