import couchbase
from couchbase.exceptions import KeyExistsError
import time
c = couchbase.Couchbase.connect(bucket='test')

e1 = dict(name='Eran Keydar',age=40) 
KEY = 'eran12'
c.set(KEY,e1)

r2 = c.lock(KEY,ttl=10)
e2 = r2.value
assert e1 == e2
e2['age'] += 1
try:
    c.unlock(KEY,r2.cas + 1)
except KeyExistsError:
    pass
c.unlock(KEY,r2.cas)
e3 = c.get(KEY).value
e3['age'] =+ 10
c.set(KEY,e3)


