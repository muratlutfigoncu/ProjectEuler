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

def circular_prime(n):
    length = len(str(n))
    new_string = str(n)
    for i in range(1,length):
        char = new_string[len(str(n))-1:len(str(n))]
        new_string = char + new_string
        if(is_prime(int(new_string[0:len(str(n))])) == False):
            return False
    return True

start = time.time()
Table = []
Sum1 = 0
Counter = 0
for i in range(1,1000000):
    if(is_prime(i) == True):
        Table.append(i)

for i in range(0, len(Table) ):
    if( circular_prime(Table[i]) == True ):
        print Table[i]
        Sum1 += Table[i]
        Counter += 1

print Sum1
print Counter
elapsed = (time.time() - start)
print "%s seconds" % (elapsed)
