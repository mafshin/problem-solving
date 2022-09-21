a = str(input("Enter the string: "))

if a.startswith("P") :
    def encode(a): 
        list1 = []
        list2 = []
        dict1 = {}
        b = (a[2:].split())
        c = set(b)
        for d in c :
            list1.append(d)
        i = 0 
        while i < len(c) :
            for x in range(len(list1)):
                dict1.update({list1[i] : x})
                i += 1
        for g in b :
            list2.append(dict1[g])
        y = list(map(lambda x : str(x) , list2))
        z = ' '.join(y)
        print(z)
        for h in dict1 :
            print(f"{h}  {dict1[h]}")
    print(encode(a))

if a.startswith("E") :
    def decode(a):
        list3 = [] 
        b = (a[2:].split())
        c = {}
        d = ""
        while d != "END" :
            d = input("Enter: ")
            c.update({d[0] : d[1:]})
        for x in b :
            list3.append(c[x])
        y = " ".join(list3)
        print(y)
    print(decode(a))