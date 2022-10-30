x=int(input("Enter the number:"))
fibo=[1,1]
i=1
while fibo[i]+fibo[i-1]<=x:
    k=fibo[i]+fibo[i-1]
    fibo.append(k)
    i+=1
print(fibo)    