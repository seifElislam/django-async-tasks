from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def send_mails(emails):
    pass


@shared_task
def save_obj(obj):
    pass
