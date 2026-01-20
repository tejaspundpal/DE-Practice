import pandas as pd

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

def increment(x):
    return x**2

df['col1'] = df['col1'].apply(increment)

print(df)


#other example 
data = {'Name': ['Tejas', 'Kedar', 'Pradeep'], 
        'Age': [25, 17, 28]}
df2 = pd.DataFrame(data)
print(df2)

def can_drive(age):
    if age >= 18:
        return 'Yes'
    else:
        return 'No'
    
df2['Can Drive'] = df2['Age'].apply(can_drive)
print(df2)    

