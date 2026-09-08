#STEP-1 LOADING A DATASET

from sklearn.datasets import load_iris
iris = load_iris()

x = iris.data
y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names

print("Feature Name:", feature_names)
print("Target Name:", target_names)