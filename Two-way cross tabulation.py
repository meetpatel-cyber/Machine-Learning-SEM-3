# Two-way cross tabulation is used to show the frequency or relationship between two categorical columns.

import pandas as pd

df = pd.read_csv("YOUR CSV FILE")
print(pd.crosstab(df.Department, df.Gender))