n = int(input("Enter the number of cities: "))

list1 = []
for m in range(n):
    m = input("Enter the city and Coordinates: ").split()
    list1.append(m)

def cities(list1):
    cities = {}
    for a in list1 :
        b = a[1:]
        c = list(map(lambda x : int(x) , b))
        cities.update({a[0] : c})
    return cities 

while True :
    o = input("Enter the cities: ")
    if o == "END" :
        break

    x = cities(list1)
    a = 1 
    sums = [] 
    while a < len(o) and o != "END":
        b = o[a]
        c = o[a - 1]
        d = x[b] 
        e = x[c] 
        d1 = d[0] - e[0] 
        e1 = d[1] - e[1] 
        a += 1
        y = (abs(d1) + abs(e1))
        sums.append(y)
    h = 0 
    for g in sums:
        h = g + h 
    print(f'{o} : {h}')