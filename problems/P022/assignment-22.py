x=int(input("Enter number of numbers:"))
list1=input("Enter numbers of first list ({} numbers):".format(x)).split()
list2=input("Enter numbers of second list ({} numbers):".format(x)).split()
list3=[]
for i in range(x):
    list1[i]=int(list1[i])
    list2[i]=int(list2[i])
    list3.append(list1[i]+list2[i])
print("sum of two list items one by one=",list3)    