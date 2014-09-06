import couchbase
import os
import json
import random
import common

cl = common.get_cl()

def main():
    add_users(1000)

def sleep(secs):
    import time
    print 'Sleeping %s seconds' % secs
    time.sleep(secs)

def read_names():
    names = []
    with open('names.txt') as fh:
        for line in fh:
            if len(line) > 2:
                name = line.split()[0]
                names.append(name)
    return names

def add_users(num):
    datas = dict()
    names = read_names()
    for x in xrange(num):
        in10 = x % 10
        chats = [1+in10,1+(in10 + 5)%10,1+(in10 + 7)%10]
        data = dict(
            id = x,
            name=random.choice(names),
            chats=chats,
            team_id=1+in10)
        datas['user:%s' % x] = data
    cl.add_multi(datas)

def users_by_docids(docids):
    kvs = cl.get_multi(docids)
    result = []
    for docid in docids:
        result.append(kvs[docid].value)
    return result

def get_team_users(team_id,skip,limit=10):
    rows = cl.query('users','by_team',key=team_id,use_devmode=True,full_set=True,stale=False,limit=limit,skip=skip)
    return [row.docid for row in rows]

def get_teams_users(team_ids,skip,limit=10):
    rows = cl.query('users','by_team',use_devmode=True,full_set=True,stale=False,limit=limit,skip=skip)
    return [row.docid for row in rows]

def get_chat_users(chat_id,skip,limit=10):
    rows = cl.query('users','by_chat',startkey=json.dumps([chat_id,'A']),use_devmode=True,full_set=True,stale=False,limit=limit,skip=skip)
    docids = [row.docid for row in rows]
    return users_by_docids(docids)

if __name__ == '__main__':
    common.flush()
    sleep(10)
    main()
