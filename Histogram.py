# Histogram using Matplotlib

import numpy as np
import matplotlib.pyplot as plt

zpoints = np.random.uniform(0.0, 5.0, 250)

plt.hist(zpoints, 5)
plt.show()