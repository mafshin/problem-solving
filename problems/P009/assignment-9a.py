import math
x=int(input("Enter a number:"))
def is_prime(n):
    if n==2:
        return True
    else:
        k=0
        s=int(math.sqrt(n))
        for i in range(3,s+1,2):
            if n%i==0:
                k=1
                break
        if k==0:
            return True
        else:
            return False
prime=[2]
for i in range (3,x+1,2):
    if is_prime(i)==True:
        prime.append(i)
print("prime numbers less than or equal with ",x," are=",prime)         
