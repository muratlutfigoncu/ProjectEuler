### Problem 28 - Number spiral diagonals ###
### Solution = 669171001
import time

start = time.time()

Global_Diag_Counter = 0
Counter = 0
i = 1
Sum1 = 0
Difference = 2
while Global_Diag_Counter < 2000:
    
    if(Counter == 4):
        Difference = Difference + 2
        Counter = 0
        
    else:
        i = i + Difference
        Sum1 = Sum1 + i
        Counter = Counter + 1
        Global_Diag_Counter = Global_Diag_Counter + 1
        ##print i


print Sum1+1 
elapsed = (time.time() - start)
print "In %s seconds" %elapsed
