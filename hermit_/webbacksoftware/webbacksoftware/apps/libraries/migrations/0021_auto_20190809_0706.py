# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-08-09 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0020_auto_20190809_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='grade',
            field=models.FloatField(default=0.0),
        ),
    ]
