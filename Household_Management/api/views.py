# -*- coding: utf8 -*-
import json
from datetime import datetime
from collections import defaultdict

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from utils.common import get_json_response

from Household_Management.api.models import HouseHold, IdCard


def get_init_data(request):
    is_out = int(request.GET.get('is_out', 0))
    res = list(HouseHold.objects.filter(is_out=is_out).values())
    return get_json_response(request, dict(init_data=res))


def get_search_data(request):
    is_out = request.GET.get('is_out', 0)
    query_parm = dict(is_out=is_out)
    for k in ['household_num', 'id', 'sex', 'nation', 'name']:
        v = request.GET.get(k, '').strip()
        if v != '':
            query_parm[k] = v
    res = list(HouseHold.objects.filter(**query_parm).values())
    return get_json_response(request, dict(search_data=res))


def check(save_parm):
    if not IdCard.objects.filter(id=save_parm['id']):
        return False, '没有相关身份证信息'
    if HouseHold.objects.filter(id=save_parm['id']):
        return False, '已存在相同身份证号'
    obj = IdCard.objects.get(id=save_parm['id'])
    for k in ['sex', 'nation', 'name', 'address']:
        if save_parm[k] != getattr(obj, k):
            return False, '与身份证信息不符'
    print save_parm['relation']
    if save_parm['relation'] == u'户主':
        if HouseHold.objects.filter(household_num=save_parm['household_num']).count() != 0:
            return False, '不能添加两个户主'
        else:
            return True, ''
    for item in HouseHold.objects.filter(household_num=save_parm['household_num']):
        if item.relation == u'户主':
            return True, ''
    return False, '没有户主信息'


def add_insert_data(request):
    save_parm = dict(is_out=0)
    for k in ['household_num', 'id', 'sex', 'nation', 'name', 'relation', 'address', 'where_in', 'date_in', 'where_out']:
        v = request.GET.get(k, '').strip()
        save_parm[k] = v
    save_parm['date_in'] = datetime.strptime(save_parm['date_in'], '%Y-%m-%d')
    status, detail = check(save_parm)
    if not status:
        return get_json_response(request, dict(status=detail))
    HouseHold(**save_parm).save()
    return get_json_response(request, dict(status='添加成功'))


def migrate(request):
    id = request.GET.get('id', '')
    household_num = request.GET.get('household_num', '')
    relation = request.GET.get('relation', '户主')
    where_out = request.GET.get('where_out', '')
    date_out = datetime.strptime(request.GET.get('date_out', ''), '%Y-%m-%d')
    if relation == u'户主':
        HouseHold.objects.filter(household_num=household_num, is_out=0).update(is_out=1, where_out=where_out, date_out=date_out)
    else:
        HouseHold.objects.filter(id=id).update(is_out=1, where_out=where_out, date_out=date_out)
    return get_json_response(request, dict(status='迁出成功'))


def get_card_init_data(request):
    res = list(IdCard.objects.all().values())
    return get_json_response(request, dict(init_data=res))


def get_card_search_data(request):
    query_param = dict()
    for k in ['id', 'sex', 'nation', 'name']:
        v = request.GET.get(k, '')
        if v != '':
            query_param[k] = v
    if len(query_param) == 0:
        res = list(IdCard.objects.all().values())
    else:
        res = list(IdCard.objects.filter(**query_param).values())
    return get_json_response(request, dict(search_data=res))


def add_card_data(request):
    save_param = dict()
    for k in ['id', 'sex', 'nation', 'name', 'address', 'born']:
        save_param[k] = request.GET.get(k)
    if IdCard.objects.filter(id=save_param['id']):
        return get_json_response(request, dict(status='已存在身份证号'))
    IdCard(**save_param).save()
    return get_json_response(request, dict(status='添加成功'))




