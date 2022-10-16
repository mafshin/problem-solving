a = input("Enter the text: ").split()

words = []
b = " "
while b != "END" :
    b = input("Enter: ")
    words.append(b)
words.remove("END")

for c in words :
    for d in range(a.count(c)):
        a.remove(c)
    for e in a :
        u = a.index(e)
        if e == (c + '.') or e == (c + ',') or e == (c + '!') or e == (c + '?') :
            a.remove(e)
            a.insert(u , e[-1])
        if e == ('"' + c + '"') or e == ("'" + c + "'") :
            a.remove(e)
x = ' '.join(a)
print(x)