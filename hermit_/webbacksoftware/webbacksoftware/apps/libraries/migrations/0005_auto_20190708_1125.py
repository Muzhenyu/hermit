# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-08 11:25
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0004_auto_20190708_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='lib_commit',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='commit of the good'),
        ),
        migrations.AlterField(
            model_name='library',
            name='lib_img',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='img of the good'),
        ),
    ]
