import couchbase
import os
import json
import random
import common
import time

cl = common.get_cl()

error_codes = ['NO_TOKEN',
               'WRONG_TOKEN',
               'WRONG_PARAM',
               'MISSING_PARAM',
               'MAPI_500']

def main():
    print 'Adding errors'
    for x in xrange(1,1000):
        dump_random_error(x)

def dump_random_error(x):
    err = dict(code=random.choice(error_codes),
             id=x,
             doctype='error')
    cl.add('error:{0}'.format(x),err)

if __name__ == '__main__':
    common.flush()
    time.sleep(10)
    main()
