# string
name = "Python"
city = 'Jabalpur'
print(name)
print(city)

# multi-line string
a = '''Python is a programming language.
It is easy to learn.
It is powerful.'''
print(a)

# accessing characters of string
print(name[0]) # first char
print(name[1]) # second char
print(name[5]) # sixth char
print(name[-1]) # sixth char
print(name[-2]) # fifth char
print(name[-6]) # first char 

# Looping through string
for char in name:
    print(char)

# Length of string
name = "iball"
print(len(name)) # find the length of string

fruit = "banana"
len1 = len(fruit)
print("Banana is a", len1, "letter word")

# String slicing
name = "cellecor,quantum" # (15 characters) 
print(name[0:8]) # 0 is first index and 8 is last index (not included 8th index character it count to n-1)
print(name[1:5]) 
print(name[:8]) # python understand string start from 0 if don't write it
print(name[9:]) # same for here it auto recognize it start from -1
print(name[:])  # if don't write any then it print whole string
print(name[0:-3]) # -3 is length - 3 = 15 - 3 = 12 
print(name[-5:-1]) 
print(name[-5:])
print(name[-4:-2])