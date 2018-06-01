# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-04 10:01
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog02', '0004_auto_20180504_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100)),
                ('Content', DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容')),
            ],
        ),
    ]