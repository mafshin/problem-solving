a = int(input("enter the first year: "))
b = int(input("enter the second year: "))
a = (a * 365)
b = (b * 365)
c = (a - b)
if (c < 0):
    print (-c)
else:
    print (+c)