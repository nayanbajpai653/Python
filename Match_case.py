# Match case 
x = int(input("enter value of x: "))
match x:                              # x is the variable to match
    case 0 :                          # if x is 0 
        print("X is Zero")             

    case 4 if x % 2 == 0 :            # case with if condition
        print("X is Four")

    case _ if x < 10:                 # empty case with if condition 
        print(x, "is < 10")
# default case (will only be matched if the above cases were not matched)
# so it basically just an else:
    case _:                            
        print(x)