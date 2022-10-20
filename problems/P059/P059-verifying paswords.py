t = int(input("Enter the number of cases: "))
punctuations = [',' , '.' , '?' , '!' , '@' , ';' , '#' , '&']
numbers = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
words = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']
for a in range(t):
    dict1 = {}
    a = input("Enter the conditions: ").split()
    for b in a :
        dict1.update({b[0] : int(b[2])})
    n = int(input("Enter the number of paswords: "))
    for m in range(n):
        m = input("Enter the pasword: ")
        num = [] 
        w = [] 
        p = [] 
        for c in m :
            for k in numbers :
                if c == k :
                    num.append(c)
            for j in punctuations:
                if c == j :
                    p.append(c)
            for f in words :
                if c == f or c == f.upper() :
                    w.append(c)
        # n = number 
        # w = words
        # l = length
        # p = punctuation
        lentgh = dict1['L'] 
        adad = dict1['N']
        horuf = dict1['W']
        alamat = dict1['P']
        if len(m) < lentgh :
            print(f'{m} length is less than {lentgh} characters.')
        elif len(p) < alamat :
            print(f'{m} must have at least {alamat} punctuation marks.')
        elif len(num) < adad :
            print(f'{m} must have at least {adad} numerics.')
        elif len(w) < horuf :
            print(f'{m} must have at least {horuf} words.')
        elif len(m) >= lentgh and len(p) >= alamat and len(num) >= adad and len(w) >= horuf :
            print(f'{m} is valid.')