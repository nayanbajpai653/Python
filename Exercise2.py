# Exercise2
''' Create a program capable of displaying questions to the user like KBC
    Display the final amount won by the user at the end of the quiz'''

print("Welcome to KBC")
print("Let's start Questions")

score = 0
q1 = "Capital of India"
o1 = ['a: Delhi', 'b: Mumbai', 'c: Indore', 'd: Goa']
a1 = 'a'
print(q1)
for i in o1:
    print(i)
ui1 = input("Enter your option a,b,c,d: ").lower()
if ui1  == a1:
    print("Rigth answer")
    score = score + 1000
else:
    print("Wrong answer !!")
    print("You loose")
    print("Final score: ", score)
    exit()

q2 = "Which planet in our solar system is known as the red planet ?"
o2 = ['a: Venus', 'b: Saturn', 'c: Jupiter', 'd: Mars']
a2 = 'd'
print(q2)
for i in o2:
    print(i)
ui2 = input("Enter your option a,b,c,d: ").lower()
if ui2 == a2:
    print("Right answer")
    score = score + 1000
else:
    print("Wrong answer !!")
    print("You loose")
    print("Final score: ", score)
    exit()

q3 = "In which country was the martial art of jiu-jitsu originally developed ?"
o3 = ['a: China', 'b: South Korea', 'c: Japan', 'd: Thailand']
a3 = 'c'
print(q3)
for i in o3:
    print(i)
ui3 = input("Enter your option a,b,c,d: ").lower()
if ui3 == a3:
    print("Right answer")
    score = score + 1000
    print("You Won :)")
    print("Final score: ", score)
else:
    print("Wrong answer !!")
    print('You loose')
    print("final score: ", score) 