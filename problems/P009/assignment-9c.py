n=int(input("Enter a number:"))
prime=[True for i in range(n+1)]
i=2
while i*i<=n:
    if prime[i]==True:
        for j in range(i*i,n+1,i):
            prime[j]=False
    i+=1
p=[]
for i in range (2,n+1):
    if prime[i]==True:
        p.append(i)    
print("prime numbers less than or equal with ",n,"=",p)    

