import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df)
print("\n")
# Comparison operators 
print(df[df['A'] == 2]) # Simple filter
print("\n")

# Boolean operators
filter = (df['A'] > 1) & (df['B'] == 6)  
print(df[filter]) # Complex filter
print("\n")

# Filters with loc accessor
filter = df['A'] > 1
print(df.loc[filter]) 
print("\n")

# isin() method
values = [2, 5]
filter = df['A'].isin(values) 
print(df[filter])