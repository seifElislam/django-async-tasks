from __future__ import absolute_import, unicode_literals
from celery import shared_task
import redis
import requests


def get_connection(host='localhost', port=6379, db=0):
    return redis.StrictRedis(host=host, port=port, db=db)


def send_request(data='', func=''):
    headers = {'content-type': 'application/json'}
    url = 'http://127.0.0.1:9000/{}/'.format(func)
    response = requests.post(url, json=data, headers=headers)
    return response.status_code

@shared_task
def handle_mails(job_id=0, mails=()):
    return 'mails are sent for job id: {}'.format(job_id)


@shared_task
def save_obj(job_id=0, obj=""):
    data = {'job_id': job_id, 'obj': obj}
    print data
    r = get_connection()
    r.incr(job_id)
    r.connection_pool.disconnect()
    send_request(data, 'save')
    return 'obj is posted for job id: {}'.format(job_id)
