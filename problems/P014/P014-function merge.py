n = int(input("Enter the first number: "))
list1 = []
for a in range(1 , (n + 1)):
    a = input("Enter the first words: ")
    list1.append(a)

m = int(input("Enter the second number: "))
list2 = []
for b in range(1 , (m + 1)):
    b = input("Enter the second words: ")
    list2.append(b)

def merge(x , y):
    list3 = x + y 
    print(list3)

print(merge(list1 , list2))