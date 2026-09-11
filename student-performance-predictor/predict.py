# Student Performance Predictor
# Make predictions for new students

import joblib
import pandas as pd
from pathlib import Path

# Load the trained model
model_path = Path(__file__).parent / "student_model.pkl"
model = joblib.load(model_path)

print("Student Performance Predictor")
print("-----------------------------")


# Function to get a valid number within a range
def get_valid_input(message, minimum, maximum):
    while True:
        try:
            value = float(input(message))

            if minimum <= value <= maximum:
                return value

            print(f"Please enter a value between {minimum} and {maximum}.")

        except ValueError:
            print("Please enter a valid number.")


# Get student information
study_hours = get_valid_input(
    "Enter study hours per day: ", 0, 24
)

attendance = get_valid_input(
    "Enter attendance percentage: ", 0, 100
)

previous_score = get_valid_input(
    "Enter previous score: ", 0, 100
)

assignment_score = get_valid_input(
    "Enter assignment score: ", 0, 100
)


# Create input data for the model
student_data = pd.DataFrame({
    "study_hours": [study_hours],
    "attendance": [attendance],
    "previous_score": [previous_score],
    "assignment_score": [assignment_score]
})


# Make prediction
prediction = model.predict(student_data)[0]


# Keep prediction between 0 and 100
prediction = max(0, min(prediction, 100))


# Display result
print("\nStudent Performance Result")
print("--------------------------")
print("Study Hours:", study_hours)
print("Attendance:", attendance)
print("Previous Score:", previous_score)
print("Assignment Score:", assignment_score)

print("\nPredicted Final Score:", round(prediction, 2))

if prediction >= 75:
    print("Performance Level: Excellent")
elif prediction >= 50:
    print("Performance Level: Good")
else:
    print("Performance Level: Needs Improvement")