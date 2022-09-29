n = int(input("Enter the 1st row of the matrix: "))
m = int(input("Enter the 1st column of the matrix: "))
p = int(input("Enter the number of columns of the 2nd matrix: "))
c = []
d = []
for a in range(n):
    a = input("Enter the numbers of 1st matrix: ").split()
    c.append(a)
for b in range(m):
    b = input("Enter the numbers of 2nd matrix: ").split()
    d.append(b)

x = list(map(lambda x : list(map(lambda y : int(y) , x)) , c))
y = list(map(lambda x : list(map(lambda y : int(y) , x)) , d))

def multiplication_matrix(x , y):

print(multiplication_matrix(x , y))