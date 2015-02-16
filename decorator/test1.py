def retry(count):
    max_x = count
    def retry_max(func):
        def _wrap(self,*args,**kwargs):
            for x in xrange(max_x):
                try:
                    return func(self,*args,**kwargs)
                except Exception,e:
                    print('Try again (%d/%d)' % (x+1,max_x))
            return func(self,*args,**kwargs)
        return _wrap
    return retry_max
                
@retry(3)
def foo(x):
    print '-------------------'
    print x
    print '-------------------'
    assert False

foo('aaa')
