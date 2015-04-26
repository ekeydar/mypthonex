#!/usr/bin/env python

from PIL import Image
import glob
import os.path
import os
import datetime

PHOTO_EXTS = ['png','jpg','jpeg']

def get_date_taken(path):
    try:
        return Image.open(path)._getexif()[36867]
    except Exception:
        return None

def get_model(path):
    """ returns the manufactor """
    try:
        return Image.open(path)._getexif()[271]
    except Exception:
        return None
        

def is_photo(f):
    fl = f.lower()
    for ext in PHOTO_EXTS:
        if fl.endswith('.' + ext):
            return True
    return False

def get_ext(f):
    return os.path.splitext(f)[1].lower().lstrip('.')


def format_date(f, dt_str, fix_to_dt):
    try:
        dt = datetime.datetime.strptime(dt_str,'%Y:%m:%d %H:%M:%S')
        if fix_to_dt:
            dt = dt + datetime.timedelta(hours=1)
        return dt.strftime('%Y_%m_%d_%H_%M_%S')
    except ValueError:
        print 'Failed to extract datetime for file %s' % f
        return dt_str.replace(':','_').replace(' ','_')

def rename_current_folder(ns):
    files = glob.glob("*")
    photo_files = [f for f in files if is_photo(f)]
    for f in photo_files:
        handle_file(f,ns)

def handle_file(f,ns):
    dt = get_date_taken(f)
    ext = get_ext(f)
    if dt:
        model = get_model(f) or 'na'
        fix_to_dt = ns.fix_to_dt and ns.fix_to_dt.lower() in model.lower()
        prefix = format_date(f,dt,fix_to_dt=fix_to_dt)
        new_name = '%s_%s.%s' % (prefix,model,ext)
        to_name = new_name
        suffix = 2
        if to_name == f:
            return
        while True:
            if os.path.exists(to_name):
                to_name = '%s_%s.%s' % (prefix,suffix,ext)
                suffix+=1
            else:
                break
        assert not os.path.exists(to_name)
        os.rename(f,to_name)
    else:
        print 'Could not get exif data for %s' % f

def main():        
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--fix_to_dt')
    ns = parser.parse_args()
    print ns
    rename_current_folder(ns)

if __name__ == '__main__':
    main()

