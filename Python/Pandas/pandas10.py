import pandas as pd

data = {'Name':['A','B','C','D'], 'Age':[10,20,30,40], 'Salary':[1000,2000,3000,4000]}
df = pd.DataFrame(data)
print(df)

print("\n")

df.insert(2,'Address',['Mumbai','Pune','Delhi','Bangalore'])
print(df)

#delete rows having salary > 2000
# df = df[df['Salary'] <= 2000]
# print(df)
print("\n")

df = df.drop(df[df['Salary'] < 2000].index)
print(df)

print("\n")
df['Role'] = ['Engineer','Manager','Director']
print(df)