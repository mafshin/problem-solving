n=int(input("Enter numbers of first list's items:"))
list1=[]
for i in range (n):
    x=input("Enter item number {}:".format(i+1))
    list1.append(x)
m=int(input("Enter numbers of second list's items:"))
list2=[]
for i in range (m):
    x=input("Enter item number {}:".format(i+1))
    list2.append(x)     
def merge(x1,x2):
    final_list=[]
    final_list.extend(x1)
    final_list.extend(x2)
    return final_list
print(merge(list1,list2))    


