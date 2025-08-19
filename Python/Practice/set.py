
#Creating a Set in Python --------------------------------------------------------------
set1 = set()
print(set1)

set1 = set("GeeksForGeeks")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# Creating a Set with the use of a tuple
tup = ("Geeks", "for", "Geeks")
print(set(tup))

# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print(set(d))

## Accessing elements in a set --------------------------------------------------------------
set1 = {3, 1, 4, 1, 5, 9, 2}

print(set1)  # Output may vary: {1, 2, 3, 4, 5, 9}

# Unindexed: Accessing elements by index is not possible
# This will raise a TypeError
try:
    print(set1[0])
except TypeError as e:
    print(e)
    
#Adding elements to a set --------------------------------------------------------------
set1 = {1, 2, 3}
print("Original set:", set1)    
set1.add(4)
print("Set after adding an element:", set1)
set1.update([5, 6])
print("Set after updating with multiple elements:", set1)    

# Removing Elements from the Set in Python---------------------------------------------------------------
# We can remove an element from a set in Python using several methods: remove(), discard() and pop(). Each method works slightly differently :

# Using remove() Method or discard() Method
# Using Remove Method
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)  

# Attempting to remove an element that does not exist
try:
    set1.remove(10)
except KeyError as e:
    print("Error:", e)  

# Using discard() Method
set1.discard(4)
print(set1)  

# Attempting to discard an element that does not exist
set1.discard(10)  # No error raised
print(set1)

# Using pop() Method
removed_element = set1.pop()
print("Set after popping an element:", set1)
print("Popped element:", removed_element)

# Using clear() Method
set1 = {1, 2, 3, 4, 5}
set1.clear()
print(set1)


#Frozen Sets in Python --------------------------------------------------------------
# A frozenset is an immutable version of a set in Python. It cannot be modified after creation.
frozen_set = frozenset([1, 2, 3, 4])
print("Frozen Set:", frozen_set)
# Attempting to add an element to a frozenset will raise an AttributeError
try:
    frozen_set.add(5)
except AttributeError as e:
    print("Error:", e)
    
#Mathematical Operations on Sets in Python --------------------------------------------------------------
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1 | set2
print("Union:", union_set)

# Intersection
intersection_set = set1 & set2
print("Intersection:", intersection_set)

# Difference
difference_set = set1 - set2
print("Difference:", difference_set)

# Symmetric Difference
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference:", symmetric_difference_set)
# Subset and Superset
print("Is set1 a subset of set2?", set1.issubset(set2))
print("Is set2 a superset of set1?", set2.issuperset(set1))