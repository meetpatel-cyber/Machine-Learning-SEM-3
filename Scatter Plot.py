# Scatter Plot using Matplotlib

import matplotlib.pyplot as plt

xpoints = [5,7,8,7,2,17,2,9,4,11,12,9,6]
ypoints = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(xpoints, ypoints)
plt.show()

# using read_csv()

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("YOUR CSV FILE")
plt.scatter(df.ID, df.GPA)
plt.title("Scatter Plot")
plt.xlabel("ID")
plt.ylabel("GPA")
plt.show()