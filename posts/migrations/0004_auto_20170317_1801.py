# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 18:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20170317_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='posts',
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
    ]