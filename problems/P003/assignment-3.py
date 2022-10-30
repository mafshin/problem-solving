x,y=input("Enter number of two years:").split()
print("x=",x)
print("y=",y)
if(x>=y) :
    z=(int(x)-int(y))*365
else:
    z=(int(y)-int(x))*365
print("The days between these two years are:",z)        