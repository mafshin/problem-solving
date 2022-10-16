n = input("Enter the numbers: ").split()
o = input("Enter the sort form: ")
m = list(map(lambda x : int(x) , n))
p = []
for x in m :
    p.append(x)


def ascending_and_descending(m , p):
    list1 = [] 
    a = 0 
    while a < len(p):
        if o == 'ASC':
            b = min(m)
            list1.append(b)
            m.remove(b)
            a += 1
        if o == 'DESC':
            c = max(m)
            list1.append(c)
            m.remove(c)
            a += 1
    return list1 
print(ascending_and_descending(m , p))