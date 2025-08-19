import pandas as pd
import sys

file = pd.read_csv(sys.stdin)
file[sys.argv[1]] = file[sys.argv[1]].str.split(pat="~")
df = file.explode(sys.argv[1])
df.to_csv(sys.stdout, index=False)
