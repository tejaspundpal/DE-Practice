# List comprehension with for loop to cube numbers
nums = [1, 2, 3, 4]
cubes = [num**3 for num in nums] 
print(cubes) # [1, 8, 27, 64]

# Generator function yields numbers one by one 
def num_sequence(n):
    for i in range(n): 
        yield i

seq = num_sequence(5)
print(next(seq)) # 0
print(next(seq)) # 1 

# Iterator from generator allows iteration
iterator = iter(num_sequence(3))
print(next(iterator)) # 0 
print(next(iterator)) # 1

# Strings are iterable 
chars = ["c" for c in "hello"]
print(chars) # ['h', 'e', 'l', 'l', 'o']