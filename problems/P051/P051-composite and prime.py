n = int(input("Enter the number: "))

def composite(n):
    for a in range(2 , n):
        b = n % a == 0 
        if b : 
            break 
    return a 
g = composite(n)

if n % g == 0 :
    print(f'{n} is a composite number')
    print(f'least prime factor of {n} is {g}')
else:
    def is_prime(m):
        p = True
        for x in range(2 , m):
            o = m % x == 0
            if o :
                p = False
                break
        return p 

    def prime_list(n):
        list1 = [2] 
        m = 3 
        while list1[-1] != n :
            if is_prime(m):
                list1.append(m)
            m += 1
        return (list1.index(n))
    h = prime_list(n)

    print(f'{n} is a prime number.')
    print(f'{n} is {h + 1}th prime number.')
    a = n - 1 
    b = n + 1 
    if (is_prime(a + 1) and is_prime(a - 1)) :
        print(f'{a} - 1 and {a} + 1 are twin prime numbers.')
    if (is_prime(b + 1) and is_prime(b - 1)) :
        print(f'{b} - 1 and {b} + 1 are twin prime numbers.')
