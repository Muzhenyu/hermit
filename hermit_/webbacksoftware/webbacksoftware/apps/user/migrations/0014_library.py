# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-13 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20190708_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
