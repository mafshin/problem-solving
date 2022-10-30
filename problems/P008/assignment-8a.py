x=int(input("Enter a number:"))
def factoriel(x):
    f=1
    for i in range (1,x+1):
        f*=i
    return f
print(x,"!=",factoriel(x))         