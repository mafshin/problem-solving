import turtle 
Hello = turtle.Turtle()
n = input("Enter the Shape and dimensions: ").split()
m = list(map(lambda x : int(x) , n[1:]))

if n[0] == "Square:" :
    def square(Hello , m):
        a = m[0]
        Hello.speed(1)
        Hello.forward(a)
        Hello.left(90)
        Hello.forward(a)
        Hello.left(90)
        Hello.forward(a)
        Hello.left(90)
        Hello.forward(a)
    print(square(Hello , m))

if n[0] == "Rectangle:" :
    def rectangle(Hello , m):
        a = m[0] 
        b = m[1]
        Hello.speed(1)
        Hello.forward(a)
        Hello.left(90)
        Hello.forward(b)
        Hello.left(90)
        Hello.forward(a)
        Hello.left(90)
        Hello.forward(b)
    print(rectangle(Hello , m))

if n[0] == "Triangle:" :
    def triangle(Hello , m):
        a = m[0] 
        Hello.speed(1)
        Hello.forward(a)
        Hello.left(120)
        Hello.forward(a)
        Hello.left(120)
        Hello.forward(a)
    print(triangle(Hello , m))

if n[0] == "Circle:" :
    def circle(Hello , m):
        a = m[0]
        Hello.speed(1)
        Hello.circle(a , 360)
    print(circle(Hello , m))

if n[0] == "Pentagon:" :
    def pentagon(Hello , m):
        a = m[0]
        Hello.speed(1)
        Hello.forward(a)
        Hello.left(72)
        Hello.forward(a)
        Hello.left(72)
        Hello.forward(a)
        Hello.left(72)
        Hello.forward(a)
        Hello.left(72)
        Hello.forward(a)
    print(pentagon(Hello , m))

if n[0] == "Oval:" :
    def oval(Hello , m):
        a = m[0]
        b = m[1]
        Hello.speed(1)
        Hello.left(45)
        Hello.circle(a , 90)
        Hello.circle(b , 90)
        Hello.circle(a , 90)
        Hello.circle(b , 90)
    print(oval(Hello , m))