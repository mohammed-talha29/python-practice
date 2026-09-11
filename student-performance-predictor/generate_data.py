import pandas as pd
import numpy as np
from pathlib import Path

# Make the results reproducible
np.random.seed(42)

# Number of students
number_of_students = 500

# Generate student data
study_hours = np.random.uniform(1, 8, number_of_students)
attendance = np.random.uniform(50, 100, number_of_students)
previous_score = np.random.uniform(40, 100, number_of_students)
assignment_score = np.random.uniform(40, 100, number_of_students)

# Calculate final score with some random variation
final_score = (
    study_hours * 4
    + attendance * 0.25
    + previous_score * 0.35
    + assignment_score * 0.30
)

# Add small random variation
final_score += np.random.normal(0, 3, number_of_students)

# Keep scores between 0 and 100
final_score = np.clip(final_score, 0, 100)

# Create a DataFrame
data = pd.DataFrame({
    "study_hours": np.round(study_hours, 2),
    "attendance": np.round(attendance, 2),
    "previous_score": np.round(previous_score, 2),
    "assignment_score": np.round(assignment_score, 2),
    "final_score": np.round(final_score, 2)
})

# Create the data folder if it doesn't exist
data_folder = Path(__file__).parent / "data"
data_folder.mkdir(exist_ok=True)

# Save the dataset
file_path = data_folder / "students.csv"
data.to_csv(file_path, index=False)

print("Dataset generated successfully!")
print("Number of students:", len(data))
print("Saved to:", file_path)