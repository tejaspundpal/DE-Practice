# Dictionary keys are case sensitive: the same name but different cases of Key will be treated distinctly.
# Keys must be immutable: This means keys can be strings, numbers or tuples but not lists.
# Keys must be unique: Duplicate keys are not allowed and any duplicate key will overwrite the previous value.
# Dictionary internally uses Hashing. Hence, operations like search, insert, delete can be performed in Constant Time.


d1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)

d = { "name": "Prajjwal", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))
print(d[(1, 2)])
print("\n")

#Remove items from dictionary
d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}

# Using del to remove an item
del d["age"]
print(d)

# Using pop() to remove an item and return the value
val = d.pop(1)
print(val)

# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
d.clear()
print(d)

#Iterating through a dictionary
d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}
for key in d:
    print(key)
    
for value in d.values():
    print(value)
    
for key, value in d.items():
    print(f"Key: {key}, Value: {value}")