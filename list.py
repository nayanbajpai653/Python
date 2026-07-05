# list
a = [5, 9, 3, "Hello", 8.5, True]
print(a)
print(type(a))

# indexing
print(a[0])    # first element 
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])    # sixth element
# print(a[6])  # error, index out of range

print(a[-1])   # last element
print(a[-3])   # third last element
print(a[-6])   # first element
# print(a[-7]) # error, index out of range

if 8.5 in a:   
    print("yes")
else:
    print("no")

if '5' in a:   # 5 is in a but it is a integer not string     
    print("yes")
else:
    print("no")

# slicing
mask = [8, 988, 6, 74, 5, 6, 1, 7, 4, 10]

print(mask[1:-1]) # from index 1 to second last index
print(mask[0:9])
print(mask[0:9:2]) # jumpindex 2
print(mask[0:9:3]) # jumpindex 3
print(mask[:5]) # from start to index 4
print(mask[2:]) # from index 2 to end
print(mask[::2]) # jumpindex 2 from start to end
print(mask[::-1]) # reverse the list

# list comprehension
lst1 = [i for i in range(4)] # [0, 1, 2, 3]
print(lst1)

lst2 = [i*i for i in range(6)]
print(lst2)

lst = [i for i in range(11) if i%2 == 0] # filter odd out
print(lst)