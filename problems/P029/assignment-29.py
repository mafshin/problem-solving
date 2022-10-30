import math
x=input("Enter numbers:").split()
sum=0
mul=1
ltn=[]
for i in range(len(x)):
    x[i]=int(x[i])
    sum+=x[i]
    mul*=x[i]
for i in range(-3,0):
    ltn.append(x[i])
mean=sum/len(x)

min=x[i]
for i in range(1,len(x)):
    if x[i]<min:
        min=x[i]
max=x[i]   
for i in range(1,len(x)):
    if x[i]>max:
        max=x[i]                       
for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            k=x[i]
            x[i]=x[j]
            x[j]=k
for i in range(len(x)):
    if len(x)%2==1:
        k=math.floor(len(x)/2)
        median=x[k]
    else:
        k=math.floor(len(x)/2)
        median=(x[k]+x[k-1])/2
print(median)        
f=[]   
for i in range(len(x)):
    if x[i]!="checked":
        t=1
        for j in range(len(x)):
            if i!=j and x[i]==x[j] :
               t+=1
               x[j]="checked"
        f.append(x[i])
        f.append(t)    
print("Max=",max,"   Min=",min,"      sum=",sum,"    mean=",mean,"    multiply=",mul,"     median=",median)
print("last three numbers=",ltn)
print(f)



            