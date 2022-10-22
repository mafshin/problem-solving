n = int(input("Enter the number: "))
a = []
p = input("Enter the numbers list: ").split()
q = list(map(lambda x : int(x) , p))
for m in range(n - 1):
    m = input("Enter the numbers list: ").split()
    o = list(map(lambda x : int(x) , m))
    a.append(o)
numbers = {'a'}
b = 0 
while b < len(q):
    for d in a :
        for e in d :
            c = q[b]
            if e == c :
                numbers.add(c)
                b += 1 
            else:
                b += 1
for f in q :
    
numbers.remove('a')
print(numbers)