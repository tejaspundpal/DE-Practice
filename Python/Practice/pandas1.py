import pandas as pd

s = pd.Series([2,3,4])

total = s.sum()
total += 10

print(total)