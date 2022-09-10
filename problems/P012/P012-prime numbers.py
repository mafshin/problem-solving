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
    list1 = [] 
    m = 2 
    while len(list1) <= n :
        if is_prime(m):
            list1.append(m)
        m += 1
    print(list1[n - 1])

print(prime_list(n))