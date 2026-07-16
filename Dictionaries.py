# Dictionaries 
dic = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
emp_id = {
    56: "Bob",
    87: "Charlie",
    349: "David"
} 

print(dic['name']) # Output: Alice
print(emp_id[87]) # Output: Charlie

print(dic.keys()) # Output: dict_keys(['name', 'age', 'city'])
print(dic.values()) # Output : dict_values(['Alice', 30, 'New York'])
print(dic.items()) # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
print(dic['age']) # Output: 30
print(dic.get('age')) # Output: 30

for key in dic.keys():
    print(dic[key])

for key, value in dic.items():
    print(key, value) 