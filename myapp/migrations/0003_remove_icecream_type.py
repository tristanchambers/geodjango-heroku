# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-02 00:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_icecream_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icecream',
            name='type',
        ),
    ]
