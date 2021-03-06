# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('password', models.CharField(max_length=60)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
