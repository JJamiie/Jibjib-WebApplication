# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 04:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jibjib', '0002_auto_20160426_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]