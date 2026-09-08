import numpy as np
from sklearn.model_selection import train_test_split

x = np.random.rand(100,5)
y = np.random.randint(0,2,100)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=1)

print("x_train:",x_train.shape)
print("x_test:",x_test.shape)
print("y_train:",y_train.shape)
print("y_test:",y_test.shape)