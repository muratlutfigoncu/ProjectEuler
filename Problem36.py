import time


def dec_to_bin(x):
    return int(bin(x)[2:])


start = time.time()

List = []
Counter = 0
Sum1 = 0
for i in range(1,1000000):
    String = str(i)
    if( String == String[::-1] and str(dec_to_bin(i)) == str(dec_to_bin(i))[::-1] ):
        List.append(String) 
        Counter = Counter + 1
        Sum1 = Sum1 + int(String)
        
print List
print Counter
print Sum1
elapsed = (time.time() - start)
print "In %s seconds" %elapsed

