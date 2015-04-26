#!/usr/bin/env python
import glob
import os.path
import os
import hashlib
from collections import defaultdict

PHOTO_EXTS = ['png','jpg','jpeg']

def compute_md5(f):
    with open(f, 'rb') as fh:
        return hashlib.md5(fh.read()).hexdigest()

def find_md5():
    files = glob.glob("*")
    md5_dict = dict()
    for idx,f in enumerate(files):
        if os.path.isfile(f):
            md5_dict[f] = compute_md5(f)
            if (idx + 1) % 10 == 0:
                print 'processed %s/%s' % (idx+1,len(files))
    return md5_dict

def find_dups():
    md5_dict = find_md5()
    dups = defaultdict(list)
    for k,v in md5_dict.iteritems():
        dups[v].append(k)
    total_dups = 0
    try:
        os.mkdir('dups')
    except Exception,e:
        pass
    for k,v in dups.iteritems():
        if len(v) > 1:
            total_dups += (len(v) - 1)
            print 'duplicates: (%s) %s' % (len(v),v)
            for dupfile in v[1:]:
                os.rename(dupfile,os.path.join('dups',dupfile))
    print 'Total duplicates: %s' % total_dups
    
if __name__ == '__main__':
    find_dups()
