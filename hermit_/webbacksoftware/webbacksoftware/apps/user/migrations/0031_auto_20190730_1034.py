# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-30 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0030_collect_library'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='user',
            name='img_url',
            field=models.CharField(default='', max_length=100, verbose_name='img_url'),
        ),
    ]
