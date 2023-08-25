def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
while True:
    print("A WORKING CALCULATOR".center(50, "-"))
    print("\n")
    a = int(input("Enter the first value > "))
    b = int(input("Enter the second value > "))
    c = input("Enter the opearater: ")
    if c == "+":
        print(add(a, b))
    elif c == "-":
        print(sub(a, b))
    elif c == "x" or c == "*":
        print(mul(a, b))
    elif c == "/":
        print(div(a, b))
