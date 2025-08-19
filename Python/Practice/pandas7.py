import pandas as pd
import numpy as np  

data = {'Fruit': ['Apple', 'Banana', 'Orange'],  
        'Price': [2.5, 1.2, 3.3]}
df = pd.DataFrame(data)
print(df)
print("\n")

avg_price = df['Price'].mean()  
print(avg_price)

filter = df['Price'] > avg_price
df.loc[filter]
print(df)
print("\n")

fruit_filter = df['Fruit'].isin(['Apple','Orange']) 
df.loc[fruit_filter]
print(df)
print("\n")