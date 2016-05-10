# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jibjib', '0002_auto_20160427_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='from_lang',
            field=models.CharField(choices=[('Thai', 'Thai'), ('English', 'English'), ('Chinese', 'Chinese')], max_length=20),
        ),
        migrations.AlterField(
            model_name='question',
            name='to_lang',
            field=models.CharField(choices=[('Thai', 'Thai'), ('English', 'English'), ('Chinese', 'Chinese')], max_length=20),
        ),
    ]
