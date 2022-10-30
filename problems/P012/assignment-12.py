import math
n=int(input("Enter a number:"))
#2 is the only even prime number so we have to fine n-1 other prime numbers
prime=[2]
k=3
while len(prime)<n:
    a=math.sqrt(k)
    i=0
    m=0
    while prime[i]<=a:
        if k%prime[i]==0:
            m=1
            break
        i+=1
    if m==0:
        prime.append(k)
    k+=2
print(n,"th prime number=",prime[n-1])            
                        