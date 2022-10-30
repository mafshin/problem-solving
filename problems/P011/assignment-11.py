x=int(input("Enter the number:"))
def fibo(n):
    if n==1 or n==0:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
i=0         
while fibo(i)<=x:
    print(fibo(i))
    i+=1
           