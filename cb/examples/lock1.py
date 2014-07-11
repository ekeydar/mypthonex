import couchbase
from couchbase.exceptions import KeyExistsError
import time
c = couchbase.Couchbase.connect(bucket='test')

e1 = dict(name='Eran Keydar',age=40) 

c.set('eran',e1)

r2 = c.lock('eran',ttl=2)
e2 = r2.value
assert e1 == e2
e2['age'] += 1
try:
    c.set('eran',e2)
except KeyExistsError:
    pass
time.sleep(3)
c.set('eran',e2)


