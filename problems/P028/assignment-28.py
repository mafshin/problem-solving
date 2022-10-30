import math
n=int(input("Enter number of cities:"))
c=input("Enter cities and their coordinations(with space between caracters):").split()
m="continue"
for i in range (0,len(c),3):
    c[i+1]=int(c[i+1])
    c[i+2]=int(c[i+2])
while(m=="continue"):
    a=input("Enter a path (with space between characters):").split()
    x=[]
    b=0
    for i in range(len(a)):
        for j in range(0,len(c),3):
            if a[i]==c[j]:
                x.append(j)
    print("x=",x)            
    for i in range(len(x)-1):
        b+=abs(c[x[i]+1]-c[x[i+1]+1])+abs(c[x[i]+2]-c[x[i+1]+2])
    print("Fuel=",b) 
    m=input("Do you want to continue?(continue/End):")             

    