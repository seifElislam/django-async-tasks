# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import string
import random
from rest_framework.decorators import api_view
from django.http import JsonResponse
from tasks import *
import redis


def get_connection(host='localhost', port=6379, db=0):
    return redis.StrictRedis(host=host, port=port, db=db)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# Create your views here.
@api_view(['POST'])
def send_mails(request):
    mails = request.data.get('mails')
    job_id = id_generator()
    handle_mails.delay(job_id, mails)
    return JsonResponse({'job id': job_id}, status=200)


@api_view(['POST'])
def save_into_db(request):
    obj = request.data.get('obj')
    job_id = id_generator()
    r = get_connection()
    r.set(job_id, 0)
    r.connection_pool.disconnect()
    save_obj.delay(job_id, obj)
    return JsonResponse({'job id': job_id}, status=200)


@api_view(['POST'])
def check_job(request):
    job_id = request.data.get('job_id')
    print 'check for job_id: {}'.format(job_id)
    r = get_connection()
    result = r.get(job_id)
    if result == '0':
        r.delete(job_id)
    r.connection_pool.disconnect()
    print 'result : {}'.format(result)
    print type(result)
    if result == '0':
        return JsonResponse({'msg': 'job is done'}, status=200)
    elif result is None:
        return JsonResponse({'msg': 'job is not found'}, status=404)
    return JsonResponse({'msg': 'job is pending'}, status=200)
