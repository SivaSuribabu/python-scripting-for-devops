import sys

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

x = float(sys.argv[1])
operation = (sys.argv[2])
y = float(sys.argv[3])

if operation == "add":
    print(add (x,y))
if operation == "sub":
    print(sub (x,y))
if operation == "mul":
    print(mul (x,y))  
if operation == "div":
    print(div (x,y))
        
