# Box Plot using Matplotlib

import matplotlib.pyplot as plt

data = [[10,12,14,15,18,20,22],
        [8,9,11,13,17,19,21],
        [14,16,18,20,23,25,27]]

plt.boxplot(data)
plt.xlabel("Group")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()

# using read_csv()

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("YOUR CSV FILE")
plt.boxplot(df.GPA)
plt.xlabel("Groups")
plt.ylabel("GPA")
plt.title("Box Plot")
plt.show()