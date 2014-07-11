import time
import redis
import threading

conn = redis.StrictRedis()

def add_user(f,l,y):
    c = conn.incr("user_counter")
    p = conn.pipeline()
    p.watch("obj_counter")
    #p.multi()
    p.set("user:%s:first" % (c),f)
    p.set("user:%s:last" % (c),l)
    p.set("user:%s:year" % (c),y)
    p.incr("obj_counter",3)
    print 'Going to execute for %s' % (f)
    res = p.execute()
    print 'for f = %s res = %s' % (f,res)

def main():
    conn.set('obj_counter',1)
    conn.flushdb()
    add_user('eran','keydar',1973)
    add_user('uri','keydar',1973)
    add_user('yuval','keydar',2006)


if __name__ == '__main__':
    main()


