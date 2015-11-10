import string, sys
import time

start = time.time()

table = []
table = [[int(n) for n in s.split()] for s in open('/Users/muratgoncu/Desktop/Triangle.txt').readlines()]


for row in range(len(table)-1, 0, -1):
    for col in range(0, row):
        table[row-1][col] += max( table[row][col] , table[row][col+1])


print table[0][0]
elapsed = (time.time() - start)
print "%s seconds" % (elapsed)
