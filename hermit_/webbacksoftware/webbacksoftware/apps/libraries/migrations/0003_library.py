# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-08 10:56
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('areas', '0001_initial'),
        ('libraries', '0002_delete_librariesinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('grade', models.FloatField()),
                ('lib_img', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='img of the good')),
                ('lib_commit', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='commit of the good')),
                ('district', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='lib_district_addresses', to='areas.Areas', verbose_name='district')),
                ('street', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='lib_street_addresses', to='areas.Areas', verbose_name='street')),
            ],
        ),
    ]
