import time
import math

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

def left_prime(n):
    for i in range(1, len(str(n))):
        n = n /10
        if( is_prime(n) == False): return False
        
    return True
    
def right_prime(n):
    for i in range(1, len(str(n))):
        String = str(n)
        String = String[::-1]
        n = int(String)/10
        String = str(n)
        String = String[::-1]
        n = int(String)
        if( is_prime(n) == False): return False
        
    return True
    
start = time.time()
Table = []
for i in range(11,1000000):
    if(is_prime(i) == True):
        Table.append(i)

#print len(Table)
sum1 = 0
for i in range(0 ,len(Table)):
    if(left_prime(Table[i]) and right_prime(Table[i])):
        #print Table[i]
        sum1 = Table[i] + sum1

print sum1
elapsed = (time.time() - start)
print "%s seconds" % (elapsed)
