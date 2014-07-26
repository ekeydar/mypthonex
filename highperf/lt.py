def l1():
    z = 0
    for x in xrange(1000):
        y = (x,x+1,x+2,x+3,x+4,x+5)
        z += sum(y)
    return z
    
    
def l2():
    z = 0
    for x in xrange(1000):
        y = [x,x+1,x+2,x+3,x+4,x+5]
        z += sum(y)
    return z


