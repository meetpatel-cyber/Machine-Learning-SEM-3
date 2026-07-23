# Scatter Plot using Week Days and Total Bill using Matplotlib

import matplotlib.pyplot as plt

x = ['Thur','Fri','Sat','Sun','Thur','Fri','Sat','Sun']
y = [170, 120, 250, 190, 160, 130, 240, 200]

plt.scatter(x,y)
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.title("Scatter Plot")
plt.show()