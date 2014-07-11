import time
import redis
import threading

conn = redis.StrictRedis()

def notrans():
    print conn.incr('notrans:')
    conn.incr('notrans:',-1)
    
def main():
    for i in xrange(4):
        t = threading.Thread(target=notrans)
        t.start()
    time.sleep(1)


if __name__ == '__main__':
    main()


