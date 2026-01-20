import pandas as pd

data = {'Name': ['John', 'Mary', 'Sarah'], 
        'Age': [25, 32, 28]}
df = pd.DataFrame(data) 

print(df)

for index, row in df.iterrows():
    print(row['Name'], row['Age'])