# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jibjib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='vote',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
