import math
x=input("Enter first number:")
y=input("Enter second number:")
k=0
a=m=len(x)-1
b=n=len(y)-1
s1=1
s2=1
for i in x:
    for f in range(m):
        s1*=10
        n=b
    for l in range(n):
        s2*=10    
    for j in y:
       k+=int(i)*int(j)*s1*s2
       s2//=10
    m-=1
    s2=1
    s1=1    
print("{}*{}={}".format(x,y,k))        
