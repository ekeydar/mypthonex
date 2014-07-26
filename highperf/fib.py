def fib():
    i,j = 0,1
    while True:
        yield i
        i,j = j,i+j


