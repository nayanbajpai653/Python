# Break and Continue Statements in Loops

for i in range(12):
    if i == 5:
        break                     # exit loop when condition hit
    print("5 X", i, "=", 5 * i)

print("Exited the loop")

for i in range(1,101,1):
    print(i, end=": ")
    if i == 50:
        break
    else:
        print("hi")
print("thank you")

for k in range(10): 
    if k == 8:
        print("Skipping the iteration when k is 8")
        continue                 # skip iteration when condition hit
    print("8 X", k, "=", 8 * k)

for i in [2, 3, 4, 5, 6, 7, 8]:
    if (i%2!=0):
        continue
    print(i)

'''  ex of Do-While loop
A set of instructions will execute at lesat once (irrespective of the condition) and 
then the repetition of the loop's body will depend on the condition passed at the end of the while loop  
'''
x = 0               
while True:          
    print(x)
    x = x + 1
    if(x%10 == 0):
        break