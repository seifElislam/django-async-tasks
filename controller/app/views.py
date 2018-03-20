# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from django.http import JsonResponse
from tasks import *


# Create your views here.
@api_view(['POST'])
def send_mails(request):
    print ">>"
    handle_mails.delay()
    return JsonResponse({'job id': 1}, status=200)


@api_view(['POST'])
def save_into_db(request):
    save_obj.delay()
    return JsonResponse({'job id': 2}, status=200)


@api_view(['POST'])
def check_job(request):
    return JsonResponse({'msg': 'job is pending'}, status=200)
