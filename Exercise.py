# Exercise 
import time
timestamp = time.strftime('%H:%M:%S')
print("Current Time:", timestamp)

if (timestamp < "12:00:00"):
    print("Good Morning")
elif (timestamp < "18:00:00"):
    print("Good afternoon")
else:
    print("Good evening")

