# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-08-02 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0011_auto_20190802_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='lib_img_url',
            field=models.CharField(max_length=100, null=True, verbose_name='img_url of the lib'),
        ),
        migrations.AlterField(
            model_name='library',
            name='lib_license_url',
            field=models.CharField(default='', max_length=100, verbose_name='lib_license_url'),
        ),
    ]
