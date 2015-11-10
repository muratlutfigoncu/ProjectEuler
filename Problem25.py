import string, sys
import time
 
start = time.time()
F1 = 1
F2 = 1
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(1,100):
    print fib(i)

elapsed = (time.time() - start)
print "%s seconds" % (elapsed)
