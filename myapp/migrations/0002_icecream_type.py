# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-02 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='type',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
