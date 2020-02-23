import pandas as pd
import numpy as np

df = pd.read_csv('data/lyrics.csv')
print(df.head)

with open('data/lyrics.txt', 'w') as f:
    for item in df.values:
        f.write("%s\n" % item)
