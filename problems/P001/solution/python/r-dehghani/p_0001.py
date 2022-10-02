def p_0001():
    num = (input("Enter the valid integer number: "))
    if isinstance(int(num), int):
        if int(num) % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

if  __name__ =="__main__":

    p_0001()