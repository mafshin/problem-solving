n = int(input("Enter the number: "))

a = [1] 
b = [1 , 1]
print(a)
print(b)
while len(a) <= n and len(b) <= n :
    if len(b) <= n :
        a = [b[0]]
        i = 0 
        while i < (len(b) - 1) :
            x = (b[i] + b[i + 1])
            a.append(x)
            i += 1
        a.append(b[-1])
        if len(a) <= n :
            print(a)
    if len(a) <= n :
        b = [a[0]]
        u = 0 
        while u < (len(a) - 1) :
            y = (a[u] + a[u + 1])
            b.append(y)
            u += 1
        b.append(a[-1])
        if len(b) <= n :
            print(b)