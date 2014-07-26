from contextlib import contextmanager
class Chat(object):
    def __init__(self,cgid):
        self.id = cgid
    def __unicode__(self):
        return 'Chatgroup %s id(self) = %s' % (self.id,id(self))

def get_chat(cgid):
    return Chat(cgid)

class myctx():
    def __init__(self,cgid):
        self.chat = get_chat(cgid)
        if cgid == 8:
            raise Exception("8 exception")
        print '__init__ %s' % (self.chat)

    def __enter__(self):
        result = self.chat
        print '__enter__ %s' % (self.chat)
        return result

    def __exit__(self, exc_type, exc_value, traceback):
        print 'Closing %s' % (self.chat)

def lock_chat(cgid):
    return myctx(cgid)

def t1():
    with lock_chat(3) as cg:
        print 'Doing %s'% cg

def t2():
    try:
        with lock_chat(4) as cg:
            raise Exception('error in params')
    except Exception,e:
        print e

def t3():
    with lock_chat(8) as cg:
        print 'should not be called'

if __name__ == '__main__':
    t1()
    print '=' * 50
    t2()
    print '=' * 50
    t3()

