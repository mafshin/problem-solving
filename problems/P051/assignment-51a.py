import math
x=int(input("Enter a number:"))
prime=[True for i in range(x+1)]
s=0
i=2
while i*i <x+1:
    if prime[i]==True:
        for j in range(i*i,x+1,i):
            prime[j]=False
            if j==x:
                s=1
                print("{} is composite number and its first prime factor is {}.".format(x,i))
    if s==1:
        break
    i+=1                          
if s==0:
    m=0
    sum=0
    for i in range(2,x+1):
        if prime[i]==True:
           m+=1
           sum+=math.log10(i)
    print("{} is a prime number ".format(x))
    print("{} is {}th prime number.".format(x,m))
    print("{} has {} decimal digits.".format(x,int(sum+1)))           
                