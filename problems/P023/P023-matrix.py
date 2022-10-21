from functools import reduce
n = int(input("Enter the 1st row of the matrix: "))
m = int(input("Enter the 1st column of the matrix: "))
p = int(input("Enter the number of columns of the 2nd matrix: "))
c = []
d = []
for a in range(n):
    a = input("Enter the numbers of 1st matrix: ").split()
    c.append(a)
for b in range(m):
    b = input("Enter the numbers of 2nd matrix: ").split()
    d.append(b)

x = list(map(lambda x : list(map(lambda y : int(y) , x)) , c))
y = list(map(lambda x : list(map(lambda y : int(y) , x)) , d))

def multiplication_matrix(x , y):
    list2 = []
    a = 0 
    while a < len(x) :
        list1 = []
        d = 0
        while d < len(x):
            b = x[a] 
            c = 0 
            e = 0 
            u = [] 
            while c < len(y) :
                f = b[e]
                g = y[c]
                h = g[d]
                u.append(f * h)
                c += 1 
                e += 1 
            k = reduce(lambda x , y : x + y , u)
            list1.append(k)
            d += 1 
        a += 1 
        list2.append(list1)
    return list2

z = multiplication_matrix(x , y) 
for o in z :
    print(o)