a = (input("Enter the first number: "))
b = int(input("Enter the second number: "))
list2 = [] 

def multiply(x , y , z):
    list1 = list(x)
    x = list(map(lambda x : int(x) , list1))
    i = 0
    h = (len(x) - 1)
    while len(x) >= (i + 1) :
        f = (x[i] * (10 ** h)) * y
        z.append(f)
        i += 1
        h -= 1

def sum(l):
    o = 0 
    for t in l :
        o = t + o 
    return o

h = multiply(a , b , list2)
print(sum(list2))