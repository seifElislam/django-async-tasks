# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=100)
