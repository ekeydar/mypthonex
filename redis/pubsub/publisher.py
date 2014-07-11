import redis
import argparse
import json

conn = redis.StrictRedis()

def send_message(kind,to,text):
    mid = conn.incr('mid')
    message = dict(kind=kind,
                   to=to,
                   text=text,
                   id=mid)
    conn.set('message:%s' % (mid),json.dumps(message))
    conn.publish("%s:%s" % (kind,to),mid)

def main():
    parser = argparse.ArgumentParser("publisher")
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument('--topic')
    g.add_argument('--user')
    parser.add_argument('--text',required=True)
    ns = parser.parse_args()
    if ns.topic:
        send_message('topic',ns.topic,ns.text)
    else:
        send_message('user',ns.user,ns.text)

if __name__ == '__main__':
    main()


