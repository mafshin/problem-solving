#BitArray
import math
import datetime
from bitarray import bitarray
x=int(input("Enter a number:"))
a=datetime.datetime.now()
prime=bitarray(x+1)
prime.setall(True)
s=0
i=3
while i*i <x+1:
    if prime[i]==True:
        for j in range(i*i,x+1,2*i):
            prime[j]=False
            if j==x:
                s=1
                print("{} is composite number and its first prime factor is {}.".format(x,i))
    if s==1:
        break
    i+=2                          
if s==0:
    m=1
    sum=math.log10(2)
    for i in range(3,x+1,2):
        if prime[i]==True:
           m+=1
           sum+=math.log10(i)
    print("{} is a prime number ".format(x))
    print("{} is {}th prime number.".format(x,m))
    print("{} has {} decimal digits.".format(x,int(sum+1))) 
b=datetime.datetime.now()
c=b-a              
print(int(c.total_seconds()))
                