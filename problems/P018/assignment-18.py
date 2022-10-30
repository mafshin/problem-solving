import math
x=int(input("Enter a number:"))
prime=[2]
couple=[]
i=3
n=0
for i in range(3,x+1,2):
    j=0
    m=0
    while prime[j]<=int(math.sqrt(i)):
        if i%prime[j]==0:
            m=1
            break
        j+=1
    if m==0:
        n+=1
        prime.append(i)
        if prime[n]-prime[n-1]==2:
           couple.append(prime[n-1])
           couple.append(prime[n])
new_list=[(couple[i],couple[i+1]) for i in range(0,len(couple),2)]                  
print("couple prime numbers less than",x,"=",new_list)    