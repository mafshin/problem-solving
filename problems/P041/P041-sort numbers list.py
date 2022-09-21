n = input("Enter the numbers: ").split()
o = input("Enter the dort form: ")
m = list(map(lambda x : int(x) , n))
p = []
for x in m :
    p.append(x)

if o == "ACS" :
    def ascending(m , p):
        list1 = [] 
        a = 0 
        while a < len(p):
            b = min(m)
            list1.append(b)
            m.remove(b)
            a += 1
        return list1 
    print(ascending(m , p))

if o == "DECS" :
    def descending(m , p):
        list1 = [] 
        a = 0 
        while a < len(p):
            b = max(m)
            list1.append(b)
            m.remove(b)
            a += 1
        return list1 
    print(descending(m , p))