# train_model.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from joblib import dump
import numpy as np

# Load sample data (Iris dataset)
iris = load_iris()
X = iris.data
y = iris.target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train a simple model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate the model
X_test_scaled = scaler.transform(X_test)
test_accuracy = model.score(X_test_scaled, y_test)
print(f"Test accuracy: {test_accuracy:.3f}")

# Save the model and scaler using joblib
dump(model, 'model.joblib', compress=3)
dump(scaler, 'scaler.joblib', compress=3)

print("Model and scaler saved successfully!")