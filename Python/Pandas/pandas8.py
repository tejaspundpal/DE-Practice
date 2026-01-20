import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [100, 200, 300]
}, index=['x', 'y', 'z'])

print("DataFrame:")
print(df)
# Using .loc (label-based)
print("Using .loc:")
print(df.loc['y', 'A'])      # Access by row label 'y' and column label 'A'
print(df.loc['x':'y', ['A']]) # Slicing by labels

# Using .iloc (position-based)
print("\nUsing .iloc:")
print(df.iloc[1, 0])         # Access by row position 1 and column position 0
print(df.iloc[0:2, [0]])     # Slicing by positions