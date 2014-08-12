class Foo(object):
    v = 100
    def __unicode__(self):
        return 'v = %s' % (self.v)

    def __repr__(self):
        return self.__unicode__()

class A(object):
    x = Foo()

class B(A):
    pass

class C(A):
    pass

if __name__ == '__main__':
    a1 = A()
    a2 = A()
    b = B()
    c = C()
    print a1.x
    print a2.x
    print b.x
    print c.x
    a1.x.v = 200
    print a1.x
    print a2.x
    print b.x
    print c.x


