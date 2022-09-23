a = input("Enter the text: ").split()

list1 = []
b = " "
while b != "END" :
    b = input("Enter: ")
    list1.append(b)
list1.remove("END")

for c in list1 :
    for d in range(a.count(c)):
        a.remove(c)
    for e in a :
        if e == (c + '.') or e == (c + ',') or e == (c + '!') or e == (c + '?') :
            a.remove(e)
x = ' '.join(a)
print(x)