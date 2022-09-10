n = int(input("Enter the 1st row of the matrix: "))
m = int(input("Enter the 1st column of the matrix: "))
p = int(input("Enter the number of columns of the 2nd matrix: "))
x = []
y = []
for a in range(n):
    a = input("Enter the numbers of 1st matrix: ").split()
    x.append(a)
for b in range(m):
    b = input("Enter the numbers of 2nd matrix: ").split()
    y.append(b)

def matrix(e , r):
    c = list(map(lambda x : list(map(lambda y : int(y) , x)) , e))
    d = list(map(lambda x : list(map(lambda y : int(y) , x)) , r))

print(matrix(x , y))