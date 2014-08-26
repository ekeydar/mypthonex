import couchbase
cb = couchbase.Couchbase()
cl = cb.connect(bucket="main")

def main():
    add_users(1000)

def add_users(num):
    datas = dict()
    for x in xrange(num):
        data = dict(
            id = x,
            name="name%s" % x,
            team_id=x%10)
        datas['user:%s' % x] = data
    cl.add_multi(datas)

def get_team_users(team_id,skip,limit=10):
    rows = cl.query('users','by_team',key=team_id,use_devmode=True,full_set=True,stale=False,limit=limit,skip=skip)
    return [row.docid for row in rows]

def get_teams_users(team_ids,skip,limit=10):
    rows = cl.query('users','by_team',use_devmode=True,full_set=True,stale=False,limit=limit,skip=skip)
    return [row.docid for row in rows]

if __name__ == '__main__':
    main()
