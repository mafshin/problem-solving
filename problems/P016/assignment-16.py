x=int(input("Enter a number:"))
for i in range(x):
    for j in range(x):
        if j<i :
           print(" ",end="")
        else:
           print("@",end="")
    print("\n")        