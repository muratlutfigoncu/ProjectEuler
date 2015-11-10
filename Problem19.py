import calendar
from datetime import *
import time
 
start = time.time()

Today = [1, 1, 1, 1900]

"""for i in range(1900,2001):
    for j in range(1,13):
        print calendar.month(i, j);
"""

Sum1 = 0
for i in range(1901,2001):
    for j in range(1,13):
        if(date(i, j, 1).weekday() == 6):
            Sum1 = Sum1 + 1
print Sum1

elapsed = (time.time() - start)
print "%s seconds" % (elapsed)
