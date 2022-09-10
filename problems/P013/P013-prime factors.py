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

def factor_list(l , n):
    factors = [] 
    for a in l :
        while n % a == 0 :
            n = n / a 
            factors.append(a)
            if n == 1 :
                break 
    return factors

u = prime_list(n)
print(factor_list(u , n))