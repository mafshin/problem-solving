import math
x=int(input("Enter a number:"))
#prime numbers under n
prime=[2]
n=int(math.sqrt(x))  
k=3
while k<=n :
    i=0
    m=0
    while prime[i]<=math.sqrt(k):
        if k%prime[i]==0:
           m=1
           break
        i+=1
    if m==0:
       prime.append(k)
    k+=2   
num=[]
m=x 
print(prime)            
for i in range(len(prime)):
    while x%prime[i]==0:
        x//=prime[i]
        num.append(prime[i])
if x!=1:
    num.append(x)        
print("prime factors of",m,"are:",num)        
