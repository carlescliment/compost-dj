# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compost', '0002_auto_20170305_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]