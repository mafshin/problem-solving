import math
x=int(input("Enter a number:"))
prime=[2]
for i in range (3,x+1,2):
    j=0
    m=0
    while prime[j]<=math.sqrt(i):
        if i%prime[j]==0:
                m=1
                break
        j+=1
    if m==0:
        prime.append(i) 
print("prime numbers less than or equal with ",x," are=",prime)               
