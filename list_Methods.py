# list Methods 
l = [5, 9, 5, 8, 2, 3, 8, 6, 8]
print(l)

l.append(7) # adds 7 at the end
print(l)

l.sort() # sorts the list
print(l)

l.sort(reverse=True) # sorts the list in descending order
print(l)

l.reverse() # reverse the list
print(l)

l.insert(3, 1) # change the value of index 3 
print(l)

print(l[1]) # gives the value at index 1

a = l.count(8) # counts how many times 8 is present in list
print(a)

 # copies the whole list and make new one 
m = l.copy()
print(m)

 # concatenation of two lists
t = [64, 84, 65] 
k = l + t        # if don't want to change the original list
print(k)

# l.extand(t)   # if want to add list in exsisting list