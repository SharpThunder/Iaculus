# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 18:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20170725_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='forum',
            new_name='category',
        ),
    ]
