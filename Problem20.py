import string, sys
import time
 
start = time.time()


def factorial(n):
    sys.maxint = 1
    for i in range(2,n+1):
        sys.maxint = sys.maxint * i
    return sys.maxint

def length(n):
    return len(str(n))

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n /= 10
    return s


print factorial(100)
print length(factorial(100))
print sum_digits(factorial(100))

elapsed = (time.time() - start)
print "%s seconds" % (elapsed)
