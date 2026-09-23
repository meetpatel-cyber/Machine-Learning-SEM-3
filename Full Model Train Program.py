# Implement Random Forest Classification

from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score 

# 2. Load a built-in dataset (The Iris Flower Dataset) 
iris = load_iris()
X = iris.data    # Features: length and width of petals/sepals 
y = iris.target  # Labels: flower species (0, 1, or 2) 

# 3. Split the data into Training (80%) and Testing (20%) sets 
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42 ) 

# 4. Initialize the machine learning model 
model = RandomForestClassifier(random_state=42) 
model.fit(X_train, y_train) 

# 5. Make predictions on the unseen test data 
predictions = model.predict(X_test) 

# 6. Evaluate the performance 
accuracy = accuracy_score(y_test, predictions) 
print(f"Model Accuracy: {accuracy * 100:.2f}%") 