n = int(input("Enter the number: "))
a = input("Enter the 1st number: ").split()
b = input("Enter the 2nd numbers: ").split()
list3 = []
c = list(map(lambda x : int(x) , a))
d = list(map(lambda x : int(x) , b))
for i in range(len(a)):
    list3.append(c[i] + d[i])
print(list3)