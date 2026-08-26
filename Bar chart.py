# A bar chart is used to compare values of different categories.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("YOUR CSV FILE")
plt.bar(df.Department, df.Age)
plt.show()