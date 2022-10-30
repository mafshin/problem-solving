def fact(n):
    if n==0 or n==1:
        return 1    
    else:
        f=n*fact(n-1)
        return f      
x=int(input("Enter a number:"))
for i in range(x):
    k=x-i+1
    while(k!=0):
        print(" ",end="")
        k-=1
    for j in range(0,i+1):
        m=fact(i)//(fact(i-j)*fact(j))
        print(m," ",end="")         
    print("\n")       