n = int(input("enter the number: "))

def is_prime(m):
    p = True  
    for x  in range (2 , m):
        o = m % x == 0 
        if o :
            p = False 
            break
    return p 

for m in range (2 , n):
    if is_prime(m):
        print(m)