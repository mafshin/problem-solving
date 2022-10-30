x=int(input("Enter a number:"))
f_list=[1]
n_list=[]
for i in range(x+1):
     print(" ",end="")
print(1,"\n")     
for i in range(1,x):
    for t in range(x-i):
        print(" ",end="")
    n_list.append(f_list[0])
    for j in range (len(f_list)-1):
        n_list.append(f_list[j]+f_list[j+1])
    if i%2==0:
        n_list.append(f_list[len(f_list)-1]*2)
        for k in range(len(n_list)):
            print(n_list[k]," ",end="")
        for m in range(len(n_list)-2,-1,-1):
                 print(n_list[m]," ",end="") 
    else:
        for k in range(len(n_list)):
            print(n_list[k]," ",end="")
        for m in range(len(n_list)-1,-1,-1):
                 print(n_list[m]," ",end="")
    f_list.clear()
    f_list.extend(n_list)
    n_list.clear()
    print("\n")                            