from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def handle_mails():
    return 'mails are sent'


@shared_task
def save_obj():
    return 'obj is saved'
