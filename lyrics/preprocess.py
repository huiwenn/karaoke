import pandas as pd
import numpy as np

df = pd.read_csv('lyrics_big.csv')
print()

with open('data/data.txt', 'w') as f:
    for item in df.lyrics.values:
        f.write("%s\n" % item)