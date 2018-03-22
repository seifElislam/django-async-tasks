# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Message
from serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework import status
import redis


def get_connection(host='localhost', port=6379, db=0):
    return redis.StrictRedis(host=host, port=port, db=db)


# Create your views here.
@api_view(['POST'])
def handle_mails(request):
    pass


@api_view(['POST'])
def save_obj(request):
    print request.data
    job_id = request.data.get('job_id')
    print 'job_id : {}'.format(job_id)
    serializer = MessageSerializer(data=request.data.get('obj'))
    if serializer.is_valid():
        time.sleep(120)
        serializer.save()
        r = get_connection()
        r.decr(job_id, 1)
        r.connection_pool.disconnect()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print 'error'
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
