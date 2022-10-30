def sum_list(x):
    sum=0
    for i in range (len(x)):
        sum+=x[i]
    print("sum of the list items:",sum)    
n=int(input("Enter the number of items:"))
my_list=[]
for i in range(n):
    x=int(input("Enter number {}:".format(i+1)))
    my_list.append(x)
sum_list(my_list)    