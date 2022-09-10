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

def twin_primes(l):
    a = 0 
    twins = []
    while a < (len(l) - 1) :
        b = l[a]
        c = l[a + 1]
        if (b + 2) == c :
            twins.append((b , c))
        a += 1 
    return twins 

i = prime_list(n)
print(twin_primes(i))