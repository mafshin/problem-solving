m = input("Enter the numbers: ").split()

n = list(map(lambda x : int(x) , m))

# def min(n):

# def max(n):

def avg(n):
    def sum(n) :
        a = 0
        for b in n :
            a = b + a
        return a
    c = len(n)
    return (sum(n)) / c

def last_numbers(n):
    a = n[-3:]
    return a
g = last_numbers(n)

def mean(n) :
    if len(n) % 2 != 0 :
        n.sort()
        b = int(len(n) / 2)
        return n[b]
    if len(n) % 2 == 0 :
        n.sort()
        b = int(len(n) / 2)
        c = n[b] + n[(b + 1)]
        return c / 2

# def highest_count(n):

def multiply(n) :
    a = 1 
    for b in n :
        a = b * a 
    return a 

print(f"Max is: ")
print(f"Min is: ")
print(f"Avg is: {(avg(n))}")
print(f"Mean is: {(mean(n))}")
print(f"Last 3 numbers are: {g}")
print(f"2 numbers with highest count are: {highest_count(n)}")
print(f"Sum of all is: {(sum(n))}")
print(f"Product of all is: {(multiply(n))}")