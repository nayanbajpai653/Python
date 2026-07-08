# Sets
s = {56, "py", 6.4, True, 8*9, 56} # set is unordered collection of items adn it do not contain duplicate items
print(type(s)) # Output: <class 'set'>
print(s)

# a = {}                           # This creates an empty dictionary, not a set
a = set()                          # Output: <class 'set'> empty set
print(type(set))

for value in s:                    # order not guaranteed
    print(s)