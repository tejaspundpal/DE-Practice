import pandas as pd

data = {'first': ['Tejas','Shubham','Kedar'],
        'last': ['Pundpal','Mehetre','Solapure'],
        'Age':['23','30','22']}

df = pd.DataFrame(data)

print(df)

df = df.rename(columns={'first':'first name','last':'last name'})
print("\n")
print(df)

print("\n")
df = df.rename(columns=str.upper)
print(df)

print("\n")

# df = df.rename(index={0:'a',1:'b',2:'c'})
# print(df)
# print("\n")

# df = df.drop(columns='LAST NAME')
# df = df.drop(index=1)
print(df)

print("\n")

# df.Age
# df
# print(df.AGE)

# df = df.AGE.astype(int)
# print(df)

# print("\n")

# df = df.reset_index(inplace=True)   
# print(df)

new_data = {'FIRST NAME':['Omya','Abhi'],
            'LAST NAME':['Shinde','Shinde'],
            'AGE':['22','23']   
}
new_data_df = pd.DataFrame(new_data)
print(new_data_df)

print("\n")

new_df = pd.concat([df,new_data_df],ignore_index=True)
print(new_df)

print("\n")
df.loc[1,'FIRST NAME'] = 'Shubhaaam'
print(df)

print("\n")
df.loc[0:1,'AGE'] = '25'
print(df)

