import time
 
start = time.time()

Max = 0
MaxLength = 0
def collatz(i):
    counter = 1
    while (i > 1):
        if (i % 2 == 0):
            i = i/2
            counter = counter + 1
        elif (i == 1):
            print "-------------------"
            if(counter > Max):
                 counter = Max
        else:
            i = 3*i + 1
            counter = counter + 1
    return counter

for n in range(1000000):
    c = collatz(n)
    if( c > Max):
        Max = c
        MaxLength = n
    
print "------------"       
print Max
print MaxLength

elapsed = (time.time() - start)
print "%s seconds" % (elapsed)
