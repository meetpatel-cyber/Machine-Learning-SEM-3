# Implement K-Nearest Neighbors (KNN) Classification

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
x = iris.data
y = iris.target
target_names = iris.target_names

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)

correct_count = 0
wrong_count = 0

for i in range(len(x_test)):
    actual_label = y_test[i]
    predicted_label = y_pred[i]
    if actual_label == predicted_label:
        correct_count += 1
    else:
        wrong_count += 1

print("\n Summary")
print("total test sample:", {len(x_test)})
print("correct prediction :", {correct_count})
print("wrong count:", {wrong_count})
print("Accuracy_score:", accuracy_score(y_test, y_pred))