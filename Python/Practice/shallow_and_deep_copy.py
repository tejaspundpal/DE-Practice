
#Shallow Copy : 
#A shallow copy creates a new object, but does not create copies of nested objects. Instead, it copies references to the original nested objects.

#Example:

import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0][0] = 99

print("Original:", original)  # Output: [[99, 2], [3, 4]]
print("Shallow:", shallow)    # Output: [[99, 2], [3, 4]]


#Deep Copy :
#A deep copy creates a new object and recursively copies all nested objects. This means changes to the copy do not affect the original.

#Example:

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 99

print("Original:", original)  # Output: [[1, 2], [3, 4]]
print("Deep:", deep)          # Output: [[99, 2], [3, 4]]

