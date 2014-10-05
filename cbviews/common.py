import couchbase
import os
import json

def get_cl():
    cb = couchbase.Couchbase()
    cl = cb.connect(bucket="main")
    return cl

def flush():
    os.system("/opt/couchbase/bin/couchbase-cli bucket-flush --cluster=localhost --bucket=main --force")

def dump_ddocs():
    dump_ddoc('users')

def dump_ddoc(ddoc):
    doc = cl.design_get(ddoc, use_devmode=True)
    with open('%s.json'%ddoc,'w') as fh:
        json.dump(doc.value,fh,indent=4)
        print 'dumped ddoc %s to %s.json' % (ddoc,ddoc)

def upload_ddoc(ddoc):
    with open('%s.json'%ddoc,'r') as fh:
        content = json.load(fh)
        cl = get_cl()
        cl.design_create(ddoc,content)
        print 'uploaded ddoc %s from %s.json' % (ddoc,ddoc)
