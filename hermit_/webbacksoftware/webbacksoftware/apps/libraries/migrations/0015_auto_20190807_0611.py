# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-08-07 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0014_auto_20190805_0718'),
    ]

    operations = [
        migrations.CreateModel(
            name='libType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=15, unique=True)),
                ('type_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='library',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='library',
            name='type',
            field=models.IntegerField(null=True),
        ),
    ]
