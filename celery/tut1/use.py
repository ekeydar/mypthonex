import tasks
import time

results = dict()
st = time.time()
for x in xrange(1,10):
    results[x] = tasks.add.delay(x,x)


not_ready = True
while not_ready:    
    time.sleep(1)
    print 'After {0:.1f} seconds'.format(time.time()-st)
    not_ready = False
    for x in xrange(1,10):
        x_ready = results[x].ready()
        print '{0} {1}'.format(x,x_ready)
        if not x_ready:
            not_ready = True
    print '----------------------------------------------'

