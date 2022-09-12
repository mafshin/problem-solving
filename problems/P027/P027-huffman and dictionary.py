a = str(input("Enter the string: "))

if a.startswith("P") :
    def encode(a): 
        list1 = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' , 'a' , 'b' , 'c' ,'d' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' , '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
        list2 = []
        b = a[2:].split()
        c = set(b)
        for d in c :
            list2.append(d)
        e = list1[:len(c)]
        print(e)
        i = 0 
        while i < len(c) :
            print(f'{list2[i]} : {e[i]}')
            i += 1

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
        print(list3)

if a.startswith("P"): 
    print(encode(a))
if a.startswith("E"):
    print(decode(a))