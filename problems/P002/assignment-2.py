def my_add():
   print(x,"+",y,"=",int(x)+int(y))
def my_sub():
    print(x,"-",y,"=",int(x)-int(y))
def my_mult():
    print(x,"*",y,"=",int(x)*int(y))
def my_div():
    print(x,"/",y,"=",int(x)/int(y))        
#x=input(print("Enter first number:"))
#y=input(print("Enter second number:"))
x,y=input("Enter two numbers:").split()
print("x= ",x)
print("y= ",y)
my_sub()
my_add()
my_mult()
my_div()
