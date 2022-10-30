import math
x=int(input("Enter a number:"))
prime=[2]
s=0
if x%2==0:
   print("{} is composite number and its first prime factor is 2".format(x))
else:
    i=3
    for i in range(3,int(math.sqrt(x)),2):
        j=0
        k=0
        while prime[j]<=int(math.sqrt(i)):
            if i%prime[j]==0:
              k=1
              break
            j+=1
        if k==0:
           prime.append(i)
           if x%i==0:
            s=1   
            print("{} is composite number and its first prime factor is {}.".format(x,i))
            break
if s==0:   #number is prime
    for i in range(prime[len(prime)-1]+2,x+1,2):
        j=0
        k=0
        while prime[j]<=int(math.sqrt(i)):
            if i%prime[j]==0:
              k=1
              break
            j+=1
        if k==0:
           prime.append(i)              
    sum=0       
    for i in range(len(prime)):
        sum+=math.log10(prime[i])
    print("{} is a prime number".format(x))
    print("{} is {}th prime number.".format(x,len(prime)))
    print("{} has {} decimal digits.".format(x,int(sum)+1))           
           
