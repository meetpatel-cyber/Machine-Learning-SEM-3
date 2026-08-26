# The fillna() function is used to replace missing GPA values with the mean GPA.

import pandas as pd

df = pd.read_csv("YOUR CSV FILE")
df.GPA = df.GPA.fillna(df.GPA.mean())
df.to_csv("YOUR CSV FILE", index=False)
print(df)