def multiply_matrices(x1,x2):
    final_list=[]
    for i in range(len(x1)):
        str=[]
        for j in range(len(x2[0])):
            m=0
            for k in range(len(x2)):
               m+=x1[i][k]*x2[k][j]
            str.append(m)
        final_list.append(str)
    print("multiply of tow matrices is=",final_list)           
#  n: first matrix row , m: first matrix column and p: second matrix coulumn
n,m,p=input("Enter three numbers:").split()
n=int(n)
m=int(m)
p=int(p)
print(n,m,p)
print
list1=[]
for i in range(n):
   str=input("Enter {} numbers of first matrix (row number {}):".format(m,i)).split()
   for j in range(len(str)):
       str[j]=int(str[j])
   list1.append(str)
list2=[]   
for i in range(m):
   str=input("Enter {} numbers of second matrix (row number {}):".format(p,i)).split()
   for j in range(len(str)):
       str[j]=int(str[j])
   list2.append(str) 
print("list1=",list1)
print("list2=",list2)
multiply_matrices(list1,list2)

  

   