import time
import redis
import threading

conn = redis.StrictRedis()

def publisher(n):
    time.sleep(1)
    for i in xrange(n):
        conn.publish('channel',i)
        time.sleep(1)
    
def run_pubsub():
    t = threading.Thread(target=publisher,args=(3,))
    t.start()
    pubsub = conn.pubsub()
    pubsub.subscribe(['channel'])
    count = 0
    for item in pubsub.listen():
        print item
        count+=1 
        if count == 4:
            pubsub.unsubscribe()
        if count == 5:
            break

if __name__ == '__main__':
    run_pubsub()


