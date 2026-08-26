# Histogram using Matplotlib

import numpy as np
import matplotlib.pyplot as plt

zpoints = np.random.uniform(0.0, 5.0, 250)
plt.hist(zpoints, 5)
plt.show()

# using read_csv()

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("YOUR CSV FILE")
plt.hist(df.GPA)
plt.title("Histogram")
plt.xlabel("GPA")
plt.ylabel("Frequency")
plt.show()