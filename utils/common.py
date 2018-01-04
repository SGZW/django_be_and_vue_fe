# -*- coding: utf8 -*-
import json
import copy
from decimal import Decimal
from datetime import datetime, date
from django.http import HttpResponse


def map_dict(d, func, pkeys=[], atom_op=None):
    if isinstance(d, (list, tuple)):
        return type(d)([map_dict(x, func, pkeys, atom_op=atom_op) for x in d])
    elif isinstance(d, dict):
        nd = {}
        for k, v in d.iteritems():
            nv = map_dict(v, func, pkeys + [k], atom_op=atom_op)
            res = func(k, nv, pkeys)
            if res is not None:
                nk, nv = func(k, nv, pkeys)
                nd[nk] = nv
        return nd
    else:
        return atom_op(d, pkeys) if atom_op else d


class MyJsonEncoder(json.JSONEncoder):
    def encode(self, obj):
        obj = map_dict(obj, func=lambda k, v, pkeys: (k, v), atom_op=bigint2str)
        return json.JSONEncoder.encode(self, obj)


INTEGER_TYPES = (int, long)


def bigint2str(obj, pkeys=None):
    if not isinstance(obj, bool) and isinstance(obj, INTEGER_TYPES):
        if type(obj) not in INTEGER_TYPES:
            # from simplejson, do not trust custom str/repr, see https://github.com/simplejson/simplejson/issues/118
            obj = int(obj)
        if (-1 << 53) < obj < (1 << 53):
            return obj
        return str(obj)
    return obj


def json_default(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    elif isinstance(obj, Decimal):
        return float(obj)
    else:
        obj_dict = copy.copy(obj.__dict__)
        if '_sa_instance_state' in obj_dict:
            del obj_dict['_sa_instance_state']
        return obj_dict


def get_json_response(request, content, *args, **kwargs):
    jsonp_callback = request.GET.get('callback')
    if jsonp_callback:
        json_ = "%s(%s)" % (jsonp_callback, json.dumps(content, default=json_default, cls=MyJsonEncoder))
    else:
        json_ = json.dumps(content, default=json_default, cls=MyJsonEncoder)
    response = HttpResponse(json_, 'application/json', *args, **kwargs)
    return response

