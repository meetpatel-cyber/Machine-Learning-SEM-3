# Scatter Plot using Day and Total Bill using Matplotlib

import matplotlib.pyplot as plt

xpoints = [1,2,3,4,5,6,7]
ypoints = [12,15,18,10,22,25,20]

plt.scatter(xpoints, ypoints)
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.title("Scatter Plot")
plt.show()