# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-06-27 06:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'user'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='gw_user',
        ),
    ]
