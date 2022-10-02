import functools


print(functools.reduce(lambda a, b: a+b,range(int(input('enter the number: '))+1)))

# this code is better seguestion for this problem

input_number = int(input('enter the number: '))

print(int((input_number*(input_number+1))/2))