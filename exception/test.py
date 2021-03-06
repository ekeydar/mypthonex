import sys
import traceback

def print_error(e):
    print 'Got exception: %s' % (e)
    print traceback.format_exc()

def main(x):
    try:
        main1(int(x))
    except Exception,e:
        print_error(e)

def main1(x1):
    x1 = x1 + 10
    main2(x1)

def main2(x2):
    x2 = x2 + 10
    main3(x2)

def main3(x3):
    x3 = x3 + 20
    main4(x3)

def main4(x4):
    x4 = x4 + 30
    main5(x4)

def main5(x5):
    x5 = x5 + 30
    main6(x5)

def main6(x6):
    if x6 > 100:
        raise Exception('%s is larger than 100' % (x6))

if __name__ == '__main__':
    main(sys.argv[1])


