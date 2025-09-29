import sys

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

x = int(sys.argv[1])
operation = sys.argv[2]
y = int(sys.argv[3])


if operation == "add":
    print(add(int(x), int(y)))
if operation == "sub":
    print(sub(int(x), int(y)))
if operation == "mul":
    print(mul(int(x), int(y)))
if operation == "div":
    print(div(int(x), int(y)))