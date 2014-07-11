import redis
import argparse
import json
import time

conn = redis.StrictRedis()

def send_message(kind,to,text):
    mid = conn.incr('mid')
    message = dict(kind=kind,
                   to=to,
                   text=text,
                   id=mid)
    conn.set('message:%s' % (mid),json.dumps(message))
    conn.publish("%s:%s" % (kind,to),mid)

def subscribe(uid,topics):
    def cb(submsg):
        msg_id = int(submsg['data'])
        msg = json.loads(conn.get('message:%s' % (msg_id)))
        print 'Got message:%s' % json.dumps(msg,indent=2)

    pubsub = conn.pubsub()
    channels = ['user:%s' % uid]
    channels.extend('topic:%s' % t for t in topics)
    channels_dict = dict((ch,cb) for ch in channels)
    pubsub.subscribe(*channels)
    #pubsub.subscribe(**channels_dict)
    #time.sleep(1000)
    for m in pubsub.listen():
        cb(m)
    
def main():
    parser = argparse.ArgumentParser("subscriber")
    parser.add_argument('--topic',nargs='+')
    parser.add_argument('--user',required=True)
    ns = parser.parse_args()
    subscribe(int(ns.user),ns.topic or [])
    
    
if __name__ == '__main__':
    main()


