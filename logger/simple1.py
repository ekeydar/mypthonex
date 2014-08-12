import logging
from threading import Thread
logging.basicConfig(filename="a.log",
               level=logging.DEBUG)

def main():
    for x in xrange(10):
        t = Thread(target=run,args=(x,))
        t.start()

def run(tid):
    for x in xrange(20):
        logging.warning("This is the first warning of %s" % tid)
        logging.error("This is the first error of %s" % tid)
        logging.debug("This is debug message of %s" % tid)

if __name__ == '__main__':
    main()

