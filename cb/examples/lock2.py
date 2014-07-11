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
c.set('eran',e2,cas=r2.cas)
e3 = c.get('eran').value
assert e3 == e2
e3['age'] =+ 10
c.set('eran',e3)


