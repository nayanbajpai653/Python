# For loop 
name = "Alice"
for i in name:
    print(i)
    if(i == "c"):
        print("Found it!")

colours = ["Red", "blue", "green", "yellow"]
for colour in colours:
    print(colour)
    for i in colour:
        print(i)

name = "Abhishek"
for i in name:
    print(i, end=", ")

for k in range(6):
    print(k)

for i in range(1, 20001):
    print(i)

for x in range(5, 51, 5):
    print(x) 