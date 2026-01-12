import numpy as np
import pandas as pd

data = {'Name': ['John', 'Mary', 'Sarah'], 
        'Age': [25, 32, 28]}
df = pd.DataFrame(data) 

print(df)

for index, row in df.iterrows():
    print(f'index : {index}, Name: {row["Name"]}, Age: {row["Age"]}')
    
print(df.info())    


random_df = pd.DataFrame({
        'A': np.random.randint(1, 100, 15),
        'B': np.random.rand(15),
        'C': np.random.choice(['X', 'Y', 'Z'], 15),
        'D': np.random.randn(15)
})

# Display first 5 rows
print("\nHead (first 5 rows):")
print(random_df.head(3))

# Display last 3 rows
print("\nTail (last 3 rows):")
print(random_df.tail(3))

# iloc - integer location based indexing
print("\niloc - Row at index 2:")
print(random_df.iloc[2])

print("\niloc - Rows 3 to 5, columns 0 to 2:")
print(random_df.iloc[3:6, 0:3])

# loc - label based indexing
print("\nloc - Rows 0 to 2, columns A and C:")
print(random_df.loc[0:2, ['A', 'C']])

# sample - random rows
print("\nsample - 3 random rows:")
print(random_df.sample(3))

# nlargest - top n rows by column value
print("\nnlargest - Top 3 rows with largest values in column A:")
print(random_df.nlargest(3, 'A'))

# nsmallest - bottom n rows by column value
print("\nnsmallest - Bottom 3 rows with smallest values in column D:")
print(random_df.nsmallest(3, 'D'))

print(random_df)

print("\n")
print(df)

df['address'] = ['Mumbai', 'Pune', 'BGL']
print(df)

df.rename(columns={'Name': 'Full_Name', 'Age': 'Age_in_Years'}, inplace=True)
print(df)

df.rename(columns=str.lower, inplace=True)
print(df)

df.rename(columns=lambda x: x + '_col', inplace=True)
print(df)

df = df.columns.str.replace('_col', '', regex=False)
print(df)