# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-08-09 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0019_imgsave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='grade',
            field=models.FloatField(default=10.0),
        ),
    ]
