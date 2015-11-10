import time

def factorial(n):
    sum1 = n
    for i in range(n, 1, -1):
        sum1 = sum1 * (i-1)
    return sum1

start = time.time()
print factorial(10)


elapsed = (time.time() - start)
print "In %s seconds" %elapsed
