import math
x=int(input("Enter a number:"))
prime=[2,3]
def prime_numbers(x,n):    #this function recognize a number is prime if not, gives the prime numbers under that
    if n==0 or n==1:
        return prime[n]
    else:   
        a=int(math.sqrt(x))
        t=2+prime[n-1]
        if t<=a:
            for i in range(t,a+1,2):
                j=0
                s=0
                while prime[j]<=int(math.sqrt(i)):
                    if i%prime[j]==0:
                        s=1
                        break
                    j+=1
                if s==0:
                    prime.append(i)
                    return i
        else:
            return x
n=0
num=[]
while x!=1:
    q=prime_numbers(x,n)
    while x%q==0:
        x//=q
        num.append(q)
    n+=1 
print(prime)
print("prime factors of",x,"=",num)                                   

   
   


