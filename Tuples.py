# Tuples
''' Tuples are immutable data types '''
tup = (65, 2, 9, 21, "first", "second", True)

print(type(tup), tup)
print(len(tup))

print(tup[0]) # first element
print(tup[-1]) # last element
print(tup[5]) # 6th element
print(tup[2:6]) # slicing from 3rd element to 6th element
print(tup[0:7])

tup2 = tup[1:4]
print(tup2)

''' tuple uses all methods of list but we cannot change the values of tuple '''

if 9 in tup:
    print('yes')
else:
    print('no')