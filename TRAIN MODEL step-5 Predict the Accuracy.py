#STEP-5 Predict the Accuracy

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

####################
from sklearn import metrics
####################

iris = load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=1)

log_reg = LogisticRegression(max_iter=200)
log_reg.fit(x_train, y_train)

print("Model trained successfully")

#########################################################

y_predict = log_reg.predict(x_test)
print(metrics.accuracy_score(y_test, y_predict))

#########################################################