# Function arguments and return statement
letter = "Hey my name is {} and I am from {}" 
name = "Alice"
place = "Wonderland"
print(letter.format(name, place)) # string formatting this way is not  feasible so f string used

print(f'Hey my name is {name} and I am from {place}')

price = 49.035202
txt = f'For only {price:.2f} dollars!'
print(txt)

print(type(f"{2 * 30}"))