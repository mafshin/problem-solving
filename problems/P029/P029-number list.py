m = input("Enter the numbers: ").split()

n = list(map(lambda x : int(x) , m))

a = max(n)
b = min(n)

def sum(l):
    z = 0 
    for x in l :
        z = x + z 
    return z 
c = (sum(n) / (len(n)))

e = n[-3:]

def multiply(l):
    x = 1 
    for q in l :
        x = q * x 
    return x 

def (l):
    l.sort()
    if len(l) % 2 != 0 :
        j = len(l) / 2 
        print(l[int(j)])
    if len(l) % 2 == 0 :
        h = int(len(l) / 2) 
        i = h + 1 
        u = int((l[h] + l[i]) / 2)
        print(u)
d = (n)


def counter(l):

g = sum(n)

h = multiply(n)

print(f"Max is {a}")
print(f"Min is {b}")
print(f"Avg is {c}")
print(f"Mean is {d}")
print(f"Last 3 numbers are {e}")
print(f"Two numbers with highest count are")
print(f"Sum of all is {g}")
print(f"Product of all is {h}")