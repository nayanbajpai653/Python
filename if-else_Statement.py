# if-else Statement
'''
Conditional operators:
> : greater than
< : less than
>= : greater than or equal to
<= : less than or equal to
== : equal to
!= : not equal to
'''

a = int(input("Enter your age: "))
if a>18:
    print("You can drive")
else:
    print("You can't drive")

appleprice = 210
budget = 200
if appleprice <= budget :
    print("You can buy the apple")
else:
    print("You can't buy apple")

num = int(input("Enter a number: "))
if num < 0:
    print("The number", num ,"is negative")
elif num == 0:
    print("The number", num ,"is zero")
else:
    print("The number", num ,"is positive")

# Nested if-else

enter = int(input("Enter a number between 0 to 20: "))
if enter < 0 :
    print("Your number is less than 0")
elif enter > 0 :
    if enter <= 10:
        print("Your number is between 0 - 10")
    if (enter > 10 and enter <= 20):
        print("Your number is between 11 - 20")
    elif enter > 20:
        print("Your number is greater than 20")
else:
    print("Your number is 0")