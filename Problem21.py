import math
import array
import time
 

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


start = time.time()

Table = [None] * 7994
Counter = 0
for i in range(1,7994):
    
    if(is_prime(i) == False):
        Table[Counter]=i
        Counter += 1
        
print Table
print len(Table)
elapsed = (time.time() - start)
print "%s seconds" % (elapsed)
