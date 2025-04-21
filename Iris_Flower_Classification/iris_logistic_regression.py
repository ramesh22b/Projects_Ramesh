# -------- Cell 1: Importing Required Libraries --------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

# -------- Cell 2: Load Dataset --------
# Load the Iris dataset CSV file
df = pd.read_csv("Iris.csv")

# -------- Cell 3: Initial Data Inspection --------
# Display basic info about the dataset
print("Dataset Info:")
print(df.info())

# -------- Cell 4: Check for Missing Values --------
# Ensure there are no missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# -------- Cell 5: Drop Unnecessary Columns --------
# Drop the 'Id' column as it is not useful for prediction
df = df.drop(columns=["Id"])

# -------- Cell 6: Visualize Class Distribution --------
# Plot the count of each iris species
sns.countplot(x='Species', data=df)
plt.title("Distribution of Iris Species")
plt.show()

# -------- Cell 7: Pairplot Visualization --------
# Visualize relationships between features
sns.pairplot(df, hue="Species")
plt.show()

# -------- Cell 8: Correlation Heatmap --------
# Plot heatmap to show feature correlations
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation")
plt.show()

# -------- Cell 9: Feature and Target Separation --------
# Separate features and labels
X = df.drop("Species", axis=1)
y = df["Species"]

# -------- Cell 10: Feature Scaling --------
# Standardize features for better performance
scaler = StandardScaler()
X = scaler.fit_transform(X)

# -------- Cell 11: Split Dataset --------
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------- Cell 12: Train Logistic Regression Model --------
# Initialize and train the model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# -------- Cell 13: Model Prediction --------
# Predict on the test set
y_pred = model.predict(X_test)

# -------- Cell 14: Evaluate Model --------
# Print accuracy, confusion matrix and classification report
print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# -------- Cell 15: Confusion Matrix Heatmap --------
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap='Blues', fmt='d')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# -------- Cell 16: Cross-Validation (Optional) --------
# Evaluate model using cross-validation
cv_scores = cross_val_score(model, X, y, cv=5)
print("\nCross-validation scores:", cv_scores)
print("Mean cross-validation accuracy:", cv_scores.mean())

# -------- Cell 17: Save Model --------
# Save the trained model to a file
joblib.dump(model, "iris_logistic_model.pkl")
print("\nModel saved as 'iris_logistic_model.pkl'")
