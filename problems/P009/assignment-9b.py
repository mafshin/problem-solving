import math
x=int(input("Enter a number:"))
prime=[2,3]
p=[]
y=1
z=-1
i=1
while y<=x or z<=x:
    y=6*i+1
    z=6*i-1
    if y<=x:
        p.append(z)
        p.append(y)
    elif z<=x:
        p.append(z)
    i+=1    
for i in range (len(p)):
    k=0
    j=0
    while prime[j]<=math.sqrt(p[i]):
        if p[i]%prime[j]==0:
            k=1
            break
        j+=1
    if k==0:
        prime.append(p[i])
print("prime numbers less than or equale with ",x," are=",prime)            



            
