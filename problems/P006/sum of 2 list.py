jack = int(input())
a = input('enter the number: ')
line = a.split(' ')
list = []
list87 = []
b = input('enter the number: ')
line1 = b.split(' ')
for x in line:
    list.append(int(x))
for u in line1:
    list87.append(int(u))
y = 0
list1399 = []
while y < jack:
    list1399.append(list[y] + list87[y])
    y += 1
print(*list1399, sep=' ')