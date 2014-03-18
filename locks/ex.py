from threading import Thread

TIMEOUT = 5

import time
def main(num):
    threads = []
    for i in xrange(num):
        t = Thread(target=go,args=(i+1,(1+i)*3))
        t.start()
        threads.append(t)
    start_time = time.time()
    print 'ALL START'
    for t in threads:
        passed_time = time.time() - start_time
        left_time = max(0.1,5 - passed_time)
        print 'left_time = %s' % (left_time)
        t.join(left_time)
    print 'AFTER JOIN'

def go(num,length):
    for i in xrange(length):
        print('[%d %d] %d' % (num,length,i))
        time.sleep(1)
    print '[%d %d] DONE' % (num,length)

if __name__ == '__main__':
    main(3)


