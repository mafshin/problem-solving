n = int(input("Enter the number: "))

def is_prime(m):
    p = True 
    for x in range(2 , m):
        o = m % x == 0 
        if o :
            p = False 
            break 
    return p 

def prime_list(n):
    primes = [] 
    for m in range(2 , n):
        if is_prime(m):
            primes.append(m)
    return primes 

def goldbach(l , f):
    for a in l :
        for b in l :
            if a + b == f :
                print(a , b)

y = prime_list(n)
print(goldbach(y , n))