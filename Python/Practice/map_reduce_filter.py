#Map, Filter, and Reduce in Python


# Function to return double of n
def double(n):
    return n * 2

# Using map to double all numbers
numbers = [5, 6, 7, 8]
result = map(double, numbers)
print(list(result))


import functools

# Define a list of numbers
numbers = [1, 2, 3, 4]

# Use reduce to compute the product of list elements
product = functools.reduce(lambda x, y: x * y, numbers)
print("Product of list elements:", product)


# Define a function to check if a number is even
def is_even(n):
    return n % 2 == 0

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to filter out even numbers
even_numbers = filter(is_even, numbers)
print("Even numbers:", list(even_numbers))