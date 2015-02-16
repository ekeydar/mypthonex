import random
import time
import pytz
import datetime

all_times = []
for x in xrange(10000):
    t = random.random() * time.time() * 1.3
    t = int(t)
    dt = datetime.datetime.utcfromtimestamp(t)
    dt = pytz.utc.localize(dt)
    assert(dt.microsecond==0)
    #dt.replace(microsecond=0)
    all_times.append((t,dt.isoformat()))

all_times1 = all_times[:]
all_times2 = all_times[:]

all_times1.sort(key=lambda x : x[0])
all_times2.sort(key=lambda x : x[1])

assert(all_times1==all_times2)



