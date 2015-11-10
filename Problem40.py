import time
import string

start = time.time()
i =1
Strng = ""
for i in range(1,185187):
     Strng += str(i)
     i = i +1

print Strng[0]
print Strng[9] 
print Strng[99] 
print Strng[999] 
print Strng[9999] 
print Strng[99999] 
print Strng[999999] 
 

Mult = int(Strng[0]) *int(Strng[9])*int(Strng[99])*int(Strng[999]) *int(Strng[9999])*int(Strng[99999])*int(Strng[999999])
print Mult
elapsed = (time.time() - start)
print "In %s seconds" %elapsed
