import math
x=int(input("Enter a number:"))
prime=[2]
m=2
for i in range(3,x+1,2):
    k=0
    for j in range(len(prime)):
        if prime[j]<=math.sqrt(i) and i%prime[j]==0:
          k=1
          break    
    if k==0:
        prime.append(i)
        print(prime)
        m*=i
print("prime=",prime)        
print(x,"#=",m)                