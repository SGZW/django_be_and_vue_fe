# -*- coding: utf8 -*-
from django.db import models


class HouseHold(models.Model):
    class Meta:
        db_table = 'household'
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    household_num = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    relation = models.CharField(max_length=255)
    nation = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    where_in = models.CharField(max_length=255)
    date_in = models.DateField()
    where_out = models.CharField(max_length=255, default='未迁出')
    date_out = models.DateField()
    is_out = models.SmallIntegerField()


class IdCard(models.Model):
    class Meta:
        db_table = 'idcard'
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    nation = models.CharField(max_length=255)
    born = models.DateField()
