# Student Performance Predictor
# Machine Learning Model Training

import pandas as pd
from pathlib import Path
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load the dataset
data_path = Path(__file__).parent / "data" / "students.csv"
data = pd.read_csv(data_path)

print("Dataset loaded successfully!")
print("\nDataset:")
print(data)

# Features (input variables)
X = data[["study_hours", "attendance", "previous_score", "assignment_score"]]

# Target (what we want to predict)
y = data["final_score"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create the Machine Learning model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Keep predictions between 0 and 100
predictions = predictions.clip(0, 100)

# Evaluate the model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Training Complete!")
print("------------------------")
print("Mean Absolute Error:", round(mae, 2))
print("R² Score:", round(r2, 2))

# Display predictions
print("\nPredictions:")
for actual, predicted in zip(y_test, predictions):
    print(
        f"Actual: {actual:.2f} | "
        f"Predicted: {predicted:.2f}"
    )
# Save the trained model
model_path = Path(__file__).parent / "student_model.pkl"
joblib.dump(model, model_path)

print("\nModel saved successfully!")