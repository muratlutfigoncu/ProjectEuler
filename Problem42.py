import time

start = time.time()

for n in range(1,101,1):
    m = ((1/2)*(n*(n+1)))
    print m


elapsed = (time.time() - start)
print "In %s seconds" %elapsed
