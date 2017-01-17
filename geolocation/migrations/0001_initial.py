# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=500)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('direction', models.CharField(max_length=500)),
                ('extra', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=500)),
                ('unique_id', models.CharField(max_length=500)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=500)),
                ('device', models.CharField(max_length=500)),
                ('extra', models.TextField(blank=True, null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geolocation.Room')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='location',
            name='user_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geolocation.UserInfo'),
        ),
    ]
