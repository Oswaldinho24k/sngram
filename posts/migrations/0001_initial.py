# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 17:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('img', models.ImageField(upload_to='/postimages')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('slug', models.SlugField(max_length=280)),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]