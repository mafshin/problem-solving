x,y=input("Enter two number:").split()
z=input("enter an operand(+ or - or * or / ):")
if z=='+':
    print(x,"+",y,"=",int(x)+int(y))
elif z=="-":
    print(x,"-",y,"=",int(x)-int(y))
elif z=="/":
     print(x,"/",y,"=",int(x)/int(y))
elif z=="*":
    print(x,"*",y,"=",int(x)*int(y))   