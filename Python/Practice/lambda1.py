square = lambda x: x ** 2
double = lambda x: x * 2
print(square(5))
print(double(5))
print("\n")

import functools

numbers = [1, 2, 3, 4, 5]

result = functools.reduce(lambda x, y: x + y, numbers)
print(result)

#lambda and map
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, nums))
print(squares)  # Output: [1, 4, 9, 16]
print("\n")

#lambda and filter
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4]
print("\n") 

#lambda and reduce
product = functools.reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24
print("\n")