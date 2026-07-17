# Dictionary methods 

ep1 = {101: 75, 267: 89, 634: 67, 852: 90} 
ep2 = {526: 85, 854: 57}

ep1.update(ep2)
print(ep1) # appending ep2 to ep1
# ep1.clear() # removes all items from ep1

info = {'name':'Karan', 'age':19, 'eligible':True}

info.pop('eligible') # removes the specified key
info.popitem() # removes the last inserted key-value pair
print(info)

del ep1[101] # removes the key 101 from ep1
print(ep1)
# del ep2 # deletes the entire dictionary ep2
# print(ep2) # raises an error as ep2 is deleted