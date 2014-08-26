import couchbase
import os

cb = couchbase.Couchbase()
cl = cb.connect(bucket="main")

def flush():
    os.system("/opt/couchbase/bin/couchbase-cli bucket-flush --cluster=localhost --bucket=main --force")

def main():
    add_users(1000)

def sleep(secs):
    import time
    print 'Sleeping %s seconds' % secs
    time.sleep(secs)

def add_users(num):
    datas = dict()
    for x in xrange(num):
        in10 = x % 10
        chats = [1+in10,1+(in10 + 5)%10,1+(in10 + 7)%10]
        c1 = chr(num + ord('A') % 26)
        c2 = chr(num + ord('A') % 26)
        data = dict(
            id = x,
            name="%s%s" % (c1,c2,x)
            chats=chats,
            team_id=1+in10)
        datas['user:%s' % x] = data
    cl.add_multi(datas)

def get_team_users(team_id,skip,limit=10):
    rows = cl.query('users','by_team',key=team_id,use_devmode=True,full_set=True,stale=False,limit=limit,skip=skip)
    return [row.docid for row in rows]

def get_teams_users(team_ids,skip,limit=10):
    rows = cl.query('users','by_team',use_devmode=True,full_set=True,stale=False,limit=limit,skip=skip)
    return [row.docid for row in rows]

def get_chat_users(chat_id,skip,limit=10):
    rows = cl.query('users','by_chat',key=chat_id,use_devmode=True,full_set=True,stale=False,limit=limit,skip=skip)

if __name__ == '__main__':
    flush()
    sleep(10)
    main()
