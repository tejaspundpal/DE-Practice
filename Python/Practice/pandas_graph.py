import pandas as pd
import matplotlib.pyplot as plt

data = {'name': ['A', 'B', 'C', 'D'], 
        'height': [160, 167, 171, 172],
        'weight': [89, 56, 68, 50]}

df = pd.DataFrame(data)
df.plot.scatter(x='height', y='weight')

plt.xlabel('Height(cm)') 
plt.ylabel('Weight(kg)')
plt.title('Height vs Weight')

plt.tight_layout()
plt.show()

def filter_height(df, min_ht, max_ht):
    return df[(df['height'] >= min_ht) & (df['height'] <= max_ht)]

result = filter_height(df, 160, 170)
print(result)