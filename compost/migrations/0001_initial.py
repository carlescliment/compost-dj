# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=2)),
                ('taken_at', models.DateTimeField(verbose_name=True)),
            ],
        ),
    ]
