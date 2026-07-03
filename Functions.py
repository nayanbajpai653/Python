# Functions 
def mean(a, b): # functions are block of code that performs a specific tasks whenever it is called
    mean = (a + b)/2
    print(mean)

def isgreater(a, b):
    if a>b:
        print(a, "is greater")
    elif b>a:
        print(b, "is greater")
    else:
        print(a, "is equal to", b)

def isless(a, b):
    if a<b:
        print(a, "is less then ", b)
    elif b<a:
        print(b, "is less then", a)
    else:
        print(a, " = ", b)
    
def greet(name):  # when use pass statement in function then it may use in future 
     pass

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
mean(a, b)
isgreater(a, b)

c = 98
d = 321.2
mean(c, d)
isgreater(c, d)