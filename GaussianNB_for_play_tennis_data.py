# Program to implement Gaussian Naive Bayes classification

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Load the dataset
play = pd.read_csv('play_tennis.csv')
x = play.drop('target', axis=1)
y = play.target

#Preprocessing
le_outlook = LabelEncoder()
x.outlook = le_outlook.fit_transform(x.outlook)

le_temperature = LabelEncoder()
x.temperature = le_temperature.fit_transform(x.temperature)

le_humidity = LabelEncoder()
x.humidity = le_humidity.fit_transform(x.humidity)

le_windy = LabelEncoder()
x.windy = le_windy.fit_transform(x.windy)

print("\nNow the Train data is:\n", x.head())

le_playTennis = LabelEncoder()
y = le_playTennis.fit_transform(y)

print("\nNow the Train output is:\n", y)

#Splitting dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#Select Model
classifier = GaussianNB()
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

print("Accuracy is:", accuracy_score(y_test, y_pred))