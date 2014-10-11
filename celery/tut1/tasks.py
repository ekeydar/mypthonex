'''
to invoke worker:
    % celery -A tasks worker --loglevel=info
'''

from celery import Celery
import time

app = Celery('tasks',
             broker='redis://localhost:6379/1',
             backend='redis://localhost:6379/1')

import redis
r = redis.StrictRedis()

ERAN = None

def get_eran():
    global ERAN
    if ERAN is None:
        ERAN = r.incr('eran1')
    return ERAN

@app.task
def add(x, y):
    print '[{0}] In add x = {0} y = {1}'.format(get_eran(),x,y)
    time.sleep(3.3)
    return x + y



	


