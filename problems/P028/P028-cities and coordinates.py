n = int(input("Enter the number of cities: "))

list1 = []
for m in range(n):
    m = input("Enter the city and Coordinates: ").split()
    list1.append(m)

def salam(list1):
    cities = {}
    for a in list1 :
        b = a[1:]
        c = list(map(lambda x : int(x) , b))
        cities.update({a[0] : c})
    return cities 

o = ""
while o != "END" :
    o = input("Enter the cities: ")

x = salam(list1)
def hello(x , o):
    a = 1 
    while a < len(o):
        b = o[a]
        c = o[a - 1]

print(hello(x , o))