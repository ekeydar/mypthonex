'''
to invoke worker:
    % celery -A tasks worker --loglevel=info
'''

from __future__ import absolute_import

from celery import Celery
import time

app = Celery('tasks',
		broker='amqp://localhost//',
		backend='amqp://localhost')

@app.task
def add(x, y):
    time.sleep(2)
    if x == y:
        raise Exception('should not be equal')
    return x + y

	


