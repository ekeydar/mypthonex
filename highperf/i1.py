def myxrange(start, stop, step=1):
    while start < stop:
        yield start 
        start += step

print sum(myxrange(1,10))

for x in myxrange(1,10):
    print x



