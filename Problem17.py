import string, sys
import time
 
start = time.time()
Words = []

def Letter_Counter(n):
    Units = ["","one","two","three","four","five","six","seven","eight","nine"]
    Teens = ["","eleven", "twelve","thirteen", "fourteen", "fifteen", "sixteen", "seventeen","eighteen", "nineteen"]
    Tens  = ["", "ten", "twenty","thirty", "forty", "fifty", "sixty", "seventy","eighty", "ninety"]
   
 
    if( len(str(n)) == 1):
        if(n == 1 or n == 2 or n == 6): Words.append(3) 
        elif(n == 3 or n == 7 or n == 8): Words.append(5)
        elif(n == 0 or n == 4 or n == 5 or n == 9): Words.append(4)
        
    elif( len(str(n)) == 2):
        if(n%10 ==0):
            if( n == 10): Words.append(3) 
            elif( n== 20 or n==30 or n == 70 or n== 80 or n==90): Words.append(6)
            elif(  n == 40 or n == 50 or n == 60 ): Words.append(5)
        elif( n>10 and n<20): Words.append(len(Teens[n%10]))
        else: Words.append(len(Tens[n/10])+len(Units[n%10]))
        
    elif( len(str(n)) == 3):
        if( (n % 100) == 0): Words.append(len(Units[n/100]) + len("hundred"))
        elif( (n %100)/10 == 0 and (n %100)%10 != 0 ): Words.append( len(Units[n/100]) + len("hundredand") + len(Units[(n %100)%10]))
        elif( (n %100)%10 == 0 and (n %100)/10 != 0 ): Words.append( len(Units[n/100]) + len("hundredand") + len(Tens[(n%100)/10]))
        elif( (n %100)/10  ==1  ): Words.append( len(Units[n/100]) + len("hundredand") + len(Teens[(n %100)%10]))
        else: Words.append( len(Units[n/100]) + len("hundredand") + len(Tens[(n %100)/10]) + len(Units[(n %100)%10]))
    elif( len(str(n)) == 4): Words.append(len("onethousand"))
        
    


    return Words

sum1 =0
for i in range(1,1001):
    Letter_Counter(i)
for i in range(len(Words)):
    sum1 = sum1 + Words[i]

print sum1+1
elapsed = (time.time() - start)
print "%s seconds" % (elapsed)
