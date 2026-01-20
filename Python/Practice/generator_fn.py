# Generator function demonstrating yield

def num_sequence(n):
    """
    Generate sequence of numbers 
    up to n yielding one at a time
    """
    i = 0
    while i < n:
        yield i 
        i += 1

# Test generator function        
seq = num_sequence(5) 

print(next(seq)) # Print next number 
print(next(seq)) # Print next number 
print(next(seq)) # Print next number 

print(list(seq)) # Materialize remaining sequence

print(seq)
print(seq)
print(seq)