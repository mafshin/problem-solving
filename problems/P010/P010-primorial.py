n = int(input("enter the number: "))

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
        for m in range(2 , n):
            if is_prime(m):
                list1.append(m)
        return list1

def multiply(l):
    r = 1
    for q in l :
        r = q * r
    return r

s = prime_list(n)
t = multiply(s)
print(t)