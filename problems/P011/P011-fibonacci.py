n = int(input("Enter the number: "))

print(1)
a = 0
b = 1
while a < n and b < n :
    if b < n :
        a = a + b 
        if a < n :
            print(a)
        if a < n :
            b = b + a
            if b < n : 
                print(b)