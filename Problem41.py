import time

def is_prime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

start = time.time()
maximum = 0
for i in range(1023456789, 9876543210):
    if(is_prime(i) == True):
        if(maximum < i):
            maximum = i
            print i

elapsed = (time.time() - start)
print "In %s seconds" %elapsed
