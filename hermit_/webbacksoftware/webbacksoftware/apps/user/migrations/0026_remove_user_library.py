# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-25 07:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_user_library'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='library',
        ),
    ]
