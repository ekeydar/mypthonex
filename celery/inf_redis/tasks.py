'''
to invoke worker:
    % celery -A tasks worker --loglevel=info
'''

from __future__ import absolute_import

from celery import Celery
import time

app = Celery('tasks',
             broker='redis://localhost:6379/1')

@app.task
def run_task(title):
    print '%s started' % (title)
    time.sleep(20)
    print '%s done' % (title)

def do_test():
    for i in xrange(10):
        title = 'TASK-%s' % (i)
        print 'Starting %s' % (title)
        run_task.delay(title)
        time.sleep(0.5)


	


