# The dropna() function is used to remove rows containing missing values from a DataFrame.

import pandas as pd

df = pd.read_csv("YOUR CSV FILE")
df = df.dropna()
df.to_csv("YOUR CSV FILE", index=False)
print(df)