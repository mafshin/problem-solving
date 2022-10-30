x=int(input("Enter a number:"))
numbers=[1]
new_list=[]
print(1)
for i in range(x):
    print(1," ",end="")
    new_list.append(1)
    for j in range(len(numbers)-1):
            print(numbers[j]+numbers[j+1]," ",end="")
            new_list.append(numbers[j]+numbers[j+1])
    new_list.append(1)
    print("1 ")
    numbers.clear()
    numbers.extend(new_list)
    new_list.clear()



                             