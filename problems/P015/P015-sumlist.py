n = int(input("Enter the number: "))
list1 = []
for a in range(1 , (n + 1)):
    a = int(input("Enter the number: "))
    list1.append(a)

def sumlist(l):
    x = 0 
    for y in l:
        x = y + x
    return x

print(sumlist(list1))