# Mean, Median, Standard Deviation and Variance using NumPy

import numpy as np

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

a = np.mean(speed)     #find mean of speed array
b = np.median(speed)   #find median of speed array
c = np.std(speed)      #find standard deviation of speed array
d = np.var(speed)      #find varience of speed array

print(a)
print(b)
print(c)
print(d)
