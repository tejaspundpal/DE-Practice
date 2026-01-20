import pandas as pd

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

def increment(x):
    return x**2

df['col1'] = df['col1'].apply(increment)

print(df)