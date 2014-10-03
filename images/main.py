from PIL import Image
import glob
import os.path
import os

PHOTO_EXTS = ['png','jpg','jpeg']

def get_date_taken(path):
    try:
        return Image.open(path)._getexif()[36867]
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

def format_date(dt):
    return dt.replace(':','_').replace(' ','_')

def rename_current_folder():
    files = glob.glob("*")
    photo_files = [f for f in files if is_photo(f)]
    for f in photo_files:
        handle_file(f)

def handle_file(f):
    dt = get_date_taken(f)
    ext = get_ext(f)
    if dt:
        prefix = format_date(dt)
        new_name = '%s.%s' % (prefix,ext)
        to_name = new_name
        suffix = 2
        if f.startswith(prefix):
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
        print f
        

if __name__ == '__main__':
    rename_current_folder()

