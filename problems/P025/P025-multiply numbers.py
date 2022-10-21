from functools import reduce

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a < b :
    s = str(b)
    d = str(a)
if a > b :
    s = str(a)
    d = str(b)
list3 = [] 

j = [[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] ,
     [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10] , 
     [0 , 2 , 4 , 6 , 8 , 10, 12, 14, 16, 18, 20] , 
     [0 , 3 , 6 , 9 , 12, 15, 18, 21, 24, 27, 30] , 
     [0 , 4 , 8 , 12, 16, 20, 24, 28, 32, 36, 40] , 
     [0 , 5 , 10, 15, 20, 25, 30, 35, 40, 45, 50] , 
     [0 , 6 , 12, 18, 24, 30, 36, 42, 48, 54, 60] , 
     [0 , 7 , 14, 21, 28, 35, 42, 49, 56, 63, 70] , 
     [0 , 8 , 16, 24, 32, 40, 48, 56, 64, 72, 80] , 
     [0 , 9 , 18, 27, 36, 45, 54, 63, 72, 81, 90] , 
     [0 , 10, 20, 30, 40, 50, 60, 70, 80, 90,100]]

def multiply(s , d , list3):
    list1 = list(s)
    list2 = list(d)
    a = list(map(lambda x : int(x) , list1))
    b = list(map(lambda x : int(x) , list2))
    c = 0 
    f = 0 
    while f < len(b) :
        u = []
        while c < len(a) :
            i = j[b[f]]
            k = i[a[c]]
            p = ('0' * ((len(b) - 1) - f))
            w = ('0' * ((len(a) - 1) - c))
            u.append(str(k) + w + p)
            c += 1 
        f += 1
        list3.append(u)
        c = 0 
    return list3

h = multiply(s , d , list3)

def numbers(h):
    list4 = []
    a = 0 
    while a < len(h):
        b = h[a]
        c = reduce(lambda x , y : int(x) + int(y) , b)
        list4.append(int(c))
        a += 1
    return list4
w = numbers(h)

def sum(l):
    o = 0 
    for t in l :
        o = t + o 
    return o

print(sum(w))