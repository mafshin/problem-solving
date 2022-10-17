n = int(input("Enter the number: "))
a = []
for m in range(n):
    m = input("Enter the numbers list: ").split()
    o = list(map(lambda x : int(x) , m))
    a.append(o)
print(a)