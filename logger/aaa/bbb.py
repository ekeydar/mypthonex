import logging
l = logging.getLogger(__name__)
l.addHandler(logging.FileHandler('foo.txt'))

l.error('From ' + __name__)



