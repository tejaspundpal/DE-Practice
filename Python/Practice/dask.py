import pandas as pd
import random
import dask.dataframe as dd

len = 100000000

data = {'a':(random.randint(0,100) for _ in range(len)),
        'b':(random.randint(0,100) for _ in range(len))}

df = pd.DataFrame(data)

print(df.head())