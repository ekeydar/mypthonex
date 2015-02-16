import couchbase
import time
import logging
logging.basicConfig(level=logging.INFO,format='[%(filename)s:%(lineno)d] %(message)s')

cl = couchbase.Couchbase.connect(host='localhost',bucket='eran',password='sismacb')

"""
There is object of kind user, each user has id (incremental int) and gid which 
denotes its group id 
Our index looks for users in specific group
The emitted key in [gid,id] (we use compound key here since its more similar
to our real case)

This is our view:

function (doc, meta) {
  if (doc.doctype == 'user') {
      emit([doc.gid,doc.id], null);
  }
}
"""

def add_to_gid(count):
    """ add count users and assign all of them with the same gid (group id) - to the next gid (e.g new one)
    """
    next_gid = cl.incr('gid:counter',initial=1).value
    ids = []
    for x in xrange(count):
        next_id = cl.incr('id:counter',initial=1).value
        ids.append(next_id)
        doc = {'gid' : next_gid,
               'doctype': 'user',
               'id' : next_id}
        cl.add('user:%s' % next_id,doc)
        
    logging.info('Added ids = %s to gid = %s',ids,next_gid)
    return next_gid
    
def go_sleep(x):
    logging.info('Go sleep %s',x)
    time.sleep(x)

def do_query(gid):
    """ query for users in group gid by looking at range [gid,0] => [gid+1,0]
    """
    startkey = [gid,0]
    endkey = [gid+1,0]
    logging.info('Doing query startkey = %s endkey = %s',startkey,endkey)
    result = list(cl.query('tests','gid',startkey=startkey,endkey=endkey))
    logging.info('Result = %s',result)
    
def main():
    gid1 = add_to_gid(5)
    gid2 = add_to_gid(5)
    gid3 = add_to_gid(5)
    go_sleep(300)
    logging.info('First query:')
    do_query(gid2) # THIS ALWAYS RETURNES EMPTY
    go_sleep(1)
    logging.info('Second query:')
    do_query(gid2) # THIS RETURNS OK

if __name__ == '__main__':
    main()

""" example output: 

[test.py:37] Added ids = [182L, 183L, 184L, 185L, 186L] to gid = 38
[test.py:37] Added ids = [187L, 188L, 189L, 190L, 191L] to gid = 39
[test.py:37] Added ids = [192L, 193L, 194L, 195L, 196L] to gid = 40
[test.py:41] Go sleep 300
[test.py:58] First query:
[test.py:49] Doing query startkey = [39L, 0] endkey = [40L, 0]
[test.py:51] Result = []
[test.py:41] Go sleep 1
[test.py:61] Second query:
[test.py:49] Doing query startkey = [39L, 0] endkey = [40L, 0]
[test.py:51] Result = [ViewRow(key=[39, 187], value=None, docid=u'user:187', doc=None), ViewRow(key=[39, 188], value=None, docid=u'user:188', doc=None), ViewRow(key=[39, 189], value=None, docid=u'user:189', doc=None), ViewRow(key=[39, 190], value=None, docid=u'user:190', doc=None), ViewRow(key=[39, 191], value=None, docid=u'user:191', doc=None)]

"""
