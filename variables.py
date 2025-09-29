def addition():
    a = 5 #locla scope variables
    b = 10 #local scope variables
    print (a + b)

def multiplication():
    x = 4
    y = 3
    print (x * y)

def subtraction():
    m = 15
    n = 7
    print(m - n)

addition()
subtraction()
multiplication()

a=5  #global scope variables
b=10 #global scope variables

def addition():
    print(a + b)
addition()
