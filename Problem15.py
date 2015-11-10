import time
import array

start = time.time()
Matrix = [[0 for x in range(40)] for x in range(40)]

for i in range(0,40):
    Matrix[i][0] = 1
for i in range(0,40):
    Matrix[0][i] = 1
for i in range(2,41):
    Matrix[1][i-1] = i
    Matrix[i-1][1] = i

#Matrix[x][y] = int(Matrix[x-1][y]) + int(Matrix[y][x-1])
for i in range (2,40,1):
    x = 2
    y = i
    while(x <= i):
        Matrix[x][y] = int(Matrix[x-1][y]) + int(Matrix[x][y-1])
        x = x + 1
        y = y - 1
        
            

#for i in range(40):
#    for j in range(40):
#        print '%s|' %Matrix[i][j],
#    print "\n"
print Matrix[20][20]


elapsed = (time.time() - start)
print "%s seconds" % (elapsed)
