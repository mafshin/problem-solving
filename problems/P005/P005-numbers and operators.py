n = int(input("Enter the number of operations: "))
for a in range(n):
    a = int(input("Enter the 1st number: "))
    b = input("Enter the operator: ")
    c = int(input("Enter the 2nd number: "))
    if b == "+" :
        print(a + c)
    elif b == "-" :
        print(a - c)
    elif b == "*" :
        print(a * c)
    elif b == "/" : 
        print(a / c)