op = print("Operations must be '+' '-' '*' '/' '//' '**' '%'")
inn = input("Enter the operations to perform: ")
value1 = 0
value2 = 0

if inn == '+' or inn == '-' or inn == '*' or inn ==  '/' or inn ==  '//' or inn ==  '**' or inn ==  '%' :
    print("plese enter two values only for operation!!")
else:
    print("Enter right operation")

for i in range(1):
    val = int(input("Enter first value: "))
    value1 += val
for i in range(1):
    val = int(input("Enter second value: "))
    value2 += val

if inn == '+':
    print(f"Result of {value1} {inn} {value2} = {value1+value2}")
elif inn == '-':
    print(f"Result of {value1} {inn} {value2} = {value1-value2}")
elif inn == '*':
    print(f"Result of {value1} {inn} {value2} = {value1*value2}")
elif inn == '/':
    print(f"Result of {value1} {inn} {value2} = {value1/value2}")
elif inn == '//':
    print(f"Result of {value1} {inn} {value2} = {value1//value2}")
elif inn == '**':
    print(f"Result of {value1} {inn} {value2} = {value1**value2}")
elif inn == '%':
    print(f"Result of {value1} {inn} {value2} = {value1%value2}")
else:
    print("ERROR!!")