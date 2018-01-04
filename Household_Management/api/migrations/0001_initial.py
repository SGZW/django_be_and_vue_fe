# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseHold',
            fields=[
                ('id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('household_num', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=255)),
                ('relation', models.CharField(max_length=255)),
                ('nation', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('where_in', models.CharField(max_length=255)),
                ('date_in', models.DateTimeField()),
                ('where_out', models.CharField(max_length=255)),
                ('date_out', models.CharField(max_length=255)),
                ('is_out', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'household',
            },
        ),
        migrations.CreateModel(
            name='IdCard',
            fields=[
                ('id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=255)),
                ('nation', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'idcard',
            },
        ),
    ]
