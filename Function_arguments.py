# Function arguments
def average(a=5, b=8):
    avg = (a+b)/2
    print(avg)

# default arguments

average()         # uses default values of a and b
average(85, 74)     # uses provided values of a and b
average(68)       # uses provided value of a and default value of b
average(b=9)      # uses default value of a and provided value of b
average(b=74, a=85)  # uses provided values of a and b

# required arguments must be passed before default arguments
'''
In case we don't pass the arguments with a key = value syntax then it is necessay
to pass the argument in the correct positional order
'''
#  when defining a function, all parameters without default values must come before any parameter with a default value.

# 1. Valid: non‑default (fname) first, then defaults
def name(fname, mname="jain", lname="kumar"):
    print("Hello", fname, mname, lname)

name("Python")                          # uses default values of middle and last
name(fname="Python", mname="murakami")  # uses default value of last
name(fname="Python", lname="jha")       # uses default value of middle 

# 2. Invalid: default (fname) before a non‑default (mname)
# def name(fname="python", mname, lname="kumar"):
    # print("Hello", fname, mname, lname)

''' we will use * before parameters and that become the keyword only so we have to write name explicitiy '''
def name(fname="python", *, mname, lname="kumar"):
    print("Hello", fname, mname, lname)

name(mname="jain")                     # uses default values of middle and last
name(mname="jain", fname="mouse")      # uses default value of last
name(mname="jain", lname="miki")       # uses default value of first

# 3. Invalid: defaults (fname, mname) before a non‑default (lname)
# def name(fname="python", mname="kumar", lname):
    # print("Hello", fname, mname, lname)

def name(fname="python", mname="kumar", *, lname):
    print("Hello", fname, mname, lname)

name(lname="kumar")                    # uses default values of middle and first
name(mname="betty",  lname="wilde")    # uses default value of first
name(fname="cento", lname="nayasa")    # uses default value of middle

# variable length arguments
'''
 pass a * before the perameter name while defining the function. The function access the arguments 
by proccessing them in front of dictionary
 '''
def average(*numbers):                        # variable length arguments stored in tuple
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i                        
    print("Average is: ", sum/len(numbers))   # sum of all variables/number of variables

average(5, 6)
average(1, 2, 3)          # passing 3 arguments
average(4, 5, 6, 7, 8)    # passing 5 arguments

def name(**name):    # keyword arguments stored in dictionary
    print(type(name))
    print("Hello,", name['fname'], name['mname'], name['lname'] ) 

name(fname='Ankit', lname='jain', mname='kumar')