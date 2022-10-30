def fact(n):
    if n==0 or n==1:
        return 1
    else:
        f=n*fact(n-1)
        return f    
x=int(input("Enter a number:"))
for i in range(x):
    for j in range(0,i+1):  
        k=fact(i)//(fact(i-j)*fact(j))
        print(k," ",end="")
    print("\n")            
