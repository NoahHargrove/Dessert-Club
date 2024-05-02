import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

# Load data from a CSV file.
test = pd.read_csv('web_app.csv')

# Extract the target variable 'dessertName' from the dataset.
y = test["dessertName"]
# Strip whitespace from the column names to prevent any issues during indexing.
test.columns = test.columns.str.strip()
# Select features for model training.
X = test[[ "cookie", "brownie", "bar", "cake", "parfait", "pie", "cupcakeMuffin", "breakfast", "heavy", "tart", "sweet", "fluffy", "gooey", "dye", "chocolate", "extraChocolate", "fudge", "peanutButter", "whiteChocolate", "butterscotch", "sprinkles", "cinnamon", "brownSugar", "powederSugar", "oreo", "cookieDough", "marshmallow", "mintMocha", "mAndMs", "pretzels", "caramel", "pumpkin", "banana", "strawberry", "blueberry", "cherry", "orange", "lemon", "carrot", "differentVegetable", "diffFruit"]]

# Split the data into training and testing sets with a 30% test size and a random seed for reproducibility.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# DECISION TREE CLASSIFIER
# Initialize a Decision Tree classifier.
dt = DecisionTreeClassifier(random_state=0)
# Fit the model on training data.
dt.fit(X_train, y_train)
# Predict on the test set.
dt_pred = dt.predict(X_test)
# Calculate and print various performance metrics.
print("Accuracy of Decision Tree Classifier: ", accuracy_score(y_test, dt_pred))
print("Precision of Decision Tree Classifier: ", precision_score(y_test, dt_pred, average='weighted', zero_division=0))
print("Recall of Decision Tree Classifier: ", recall_score(y_test, dt_pred, average='weighted', zero_division=0))
print("F1-Score of Decision Tree Classifier: ", f1_score(y_test, dt_pred, average='weighted', zero_division=0))

# KNN CLASSIFIER
# Initialize a K-Nearest Neighbors classifier with 5 neighbors.
knn = KNeighborsClassifier(n_neighbors=5)
# Fit the model on training data.
knn.fit(X_train, y_train)
# Predict on the test set.
knn_pred = knn.predict(X_test)
# Calculate and print various performance metrics.
print("Accuracy of KNN Classifier: ", accuracy_score(y_test, knn_pred))
print("Precision of KNN Classifier: ", precision_score(y_test, knn_pred, average='weighted', zero_division=0))
print("Recall of KNN Classifier: ", recall_score(y_test, knn_pred, average='weighted', zero_division=0))
print("F1-Score of KNN Classifier: ", f1_score(y_test, knn_pred, average='weighted', zero_division=0))

# SVM CLASSIFIER
# Initialize a Support Vector Machine classifier with a linear kernel.
svm = SVC(kernel='linear', probability=True, random_state=0)  # Using linear for simplicity, probability=True enables predict_proba
# Fit the model on training data.
svm.fit(X_train, y_train)
# Predict on the test set.
svm_pred = svm.predict(X_test)
# Calculate and print various performance metrics.
print("Accuracy of SVM Classifier: ", accuracy_score(y_test, svm_pred))
print("Precision of SVM Classifier: ", precision_score(y_test, svm_pred, average='weighted', zero_division=0))
print("Recall of SVM Classifier: ", recall_score(y_test, svm_pred, average='weighted', zero_division=0))
print("F1-Score of SVM Classifier: ", f1_score(y_test, svm_pred, average='weighted', zero_division=0))

# RANDOM FOREST CLASSIFIER
# Initialize a Random Forest classifier with 100 trees.
rf = RandomForestClassifier(n_estimators=100, random_state=0)  # 100 trees
# Fit the model on training data.
rf.fit(X_train, y_train)
# Predict on the test set.
rf_pred = rf.predict(X_test)
# Calculate and print various performance metrics.
print("Accuracy of Random Forest Classifier: ", accuracy_score(y_test,
