import pandas as pd
import joblib
from pathlib import Path

# Load the dataset
data_path = Path(__file__).parent / "data" / "students.csv"
data = pd.read_csv(data_path)

# Load the trained model
model_path = Path(__file__).parent / "student_model.pkl"
model = joblib.load(model_path)

# Features
X = data[[
    "study_hours",
    "attendance",
    "previous_score",
    "assignment_score"
]]

# Actual final scores
y = data["final_score"]

# Make predictions
predictions = model.predict(X)

# Add predictions to the dataset
data["predicted_score"] = predictions

# Calculate prediction error
data["error"] = data["final_score"] - data["predicted_score"]

# Calculate absolute error
data["absolute_error"] = data["error"].abs()

# Find the 10 students with the largest errors
largest_errors = data.sort_values(
    "absolute_error",
    ascending=False
).head(10)

# Display results
print("Top 10 Students with Largest Prediction Errors")
print("-----------------------------------------------")

print(
    largest_errors[[
        "study_hours",
        "attendance",
        "previous_score",
        "assignment_score",
        "final_score",
        "predicted_score",
        "error",
        "absolute_error"
    ]].round(2).to_string(index=False)
)

# Plot actual vs predicted scores
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))

plt.scatter(
    data["final_score"],
    data["predicted_score"]
)

# Perfect prediction reference line
plt.plot(
    [0, 100],
    [0, 100],
    linestyle="--"
)

plt.xlabel("Actual Final Score")
plt.ylabel("Predicted Final Score")
plt.title("Actual vs Predicted Final Scores")

plt.show()