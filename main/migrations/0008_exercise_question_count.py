# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-22 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_attempt'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='question_count',
            field=models.IntegerField(default=20),
        ),
    ]