# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-06 03:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='city',
        ),
        migrations.RemoveField(
            model_name='address',
            name='district',
        ),
        migrations.RemoveField(
            model_name='address',
            name='province',
        ),
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
