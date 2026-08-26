# A CSV file can be saved with TAB as the separator instead of a comma using sep='\t'.

import pandas as pd

df = pd.read_csv("YOUR CSV FILE")
df.to_csv('output.tsv', sep='\t', index=False)
print("Done")