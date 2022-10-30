x=int(input("Enter a number:"))
for i in range(x+1):
    for j in range(x):
        if j<i:
            print("0",end="")
        else:
            print("+",end="")    
    print("\n")