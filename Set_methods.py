s1 = {2, 5, 7, 9}
s2 = {1, 2, 7, 4, 5}

print(s1.union(s2)) # Output: {1, 2, 4, 5, 7, 9}
s1.update(s2) 
print(s1, s2) # Output: {1, 2, 4, 5, 7, 9} {1, 2, 7, 4, 5}

cities = {"New York", "London", "Mumbai", "Tokyo"}
cities2 = {"Delhi", "Tokyo", "London"}

print(cities.intersection(cities2)) # Output: {'Tokyo', 'London'}

print(cities.intersection_update(cities2)) # Output: {'Tokyo', 'London'}
print(cities) # Output: {'Tokyo', 'London'}

print(cities.symmetric_difference(cities2)) # Output: {'New York', 'Mumbai', 'Delhi'}
print(cities.difference(cities2)) # Output: {'New York', 'Mumbai'}
print(cities.difference_update(cities2)) # Output: {'New York', 'Mumbai'}

cities = {"New York", "London", "Mumbai", "Tokyo"}
cities2 = {"Tokyo", "London"}
cities3 = cities.copy()

print(cities.isdisjoint(cities2)) # Output: False
print(cities.superset(cities2)) # Output: True
print(cities.issubset(cities2)) # Output: False
print(cities2.issubset(cities)) # Output: True
print(cities2.superset(cities)) # Output: False

cities.add("Delhi")
print(cities) # Output: {'New York', 'London', 'Mumbai', 'Tokyo', 'Delhi'}

cities.remove("London")
print(cities) # Output: {'New York', 'Mumbai', 'Tokyo', 'Delhi'}

cities.discard("Tokyo")
print(cities) # Output: {'New York', 'Mumbai', 'Delhi'} 

cities.update(["Bangalore", "Chennai"])
print(cities) # Output: {'New York', 'Mumbai', 'Delhi', 'Bangalore', 'Chennai'}

cities.pop()
print(cities) # Output: {'Mumbai', 'Delhi', 'Bangalore', 'Chennai'}     

del cities3  # deletes the entire set   
# print(cities3) # Output: {'Mumbai', 'Delhi', 'Bangalore', 'Chennai'}

cities.clear()
print(cities) # Output: set()

if "London" in cities:
    print("Present")
else:
    print("Not found") # Output: Not found