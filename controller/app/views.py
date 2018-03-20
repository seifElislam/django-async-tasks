# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse


# Create your views here.
@api_view(['POST'])
def send_mails(request):
    pass


@api_view(['POST'])
def save_into_db(request):
    pass
