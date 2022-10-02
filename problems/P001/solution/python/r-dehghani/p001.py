def solution():
    num = input("Enter the valid number: ")
    if isinstance(int(num), int):
        if int(num) % 2 == 0:
            print(f"{num} is even")
        else :
            print(f"{num} is odd")

if __name__ == "__main__":
    solution()