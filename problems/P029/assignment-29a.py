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
        k=int(len(x)/2)
        median=x[k]
    else:
        k=int(len(x)/2)
        median=(x[k]+x[k+1])//2        
f=[] 
m=[0,0,0,0]  
for i in range(len(x)):
    if x[i]!="checked":
        t=1
        for j in range(len(x)):
            if i!=j and x[i]==x[j] :
               t+=1
               x[j]="checked"
        f.append(x[i])
        f.append(t)       
        if t>m[1]:
            print(x[i])
            m[2]=m[0]
            m[3]=m[1]
            m[1]=t
            m[0]=x[i]
        elif t>m[3] and t<=m[1]:
             m[3]=t
             m[2]=x[i]
print("Max=",max,"   Min=",min,"      sum=",sum,"    mean=",mean,"    multiply=",mul,"     median=",median)
print("last three numbers=",ltn)
print(f)
print(m)
if m[1]==1:
    print("any number is repeated more than one time.")
elif m[3]==1:
    print(m[0],"is repeated",m[1],"times and all other numbers just one time")
else:
    print(m[0],"is repeated",m[1],"times",m[2],"is repeated",m[3],"times.")
