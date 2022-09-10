a = str(input("Enter the string: "))

if a.startswith("P") :
    def encode(a):
        b = (a[2:]).split()
        list1 = []
        for x in range(len(b)):
            y = x , b[x]
            list1.append(x)
            print(y)
        print(list1)

if a.startswith("E") :
    def decode(a):
        list2 = []
        b = ""
        while b != "END" :
            b = input("Enter: ")
            c = b[1:]
            list2.append(c)
        print(list2[:-1])

if a.startswith("P") :
    print(encode(a))
elif a.startswith("E") :
    print(decode(a))