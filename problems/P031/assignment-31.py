x=int(input("Enter a number:"))
prime=[True for i in range(x+1)]
prime[0]=False
prime[1]=False
i=2
while i*i <= x:
      if prime[i]==True:
        for j in range(i*i,x+1,i):
            prime[j]=False
      i+=1
k=[]
m=0      
for i in range(x):
    if prime[i]==True:
        k.append(i)
for i in range(len(k)):
    for j in range(len(k)-1,-1,-1):
        if k[i]+k[j]==x:
            print(k[i],k[j])
            m=1
            break
    if m==1:
        break                               

