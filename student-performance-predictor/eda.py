import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load the dataset
data_path = Path(__file__).parent / "data" / "students.csv"
df = pd.read_csv(data_path)

# 1. Study hours vs final score
plt.figure()
plt.scatter(df["study_hours"], df["final_score"])
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")
plt.show()

# 2. Previous score vs final score
plt.figure()
plt.scatter(df["previous_score"], df["final_score"])
plt.xlabel("Previous Score")
plt.ylabel("Final Score")
plt.title("Previous Score vs Final Score")
plt.show()

# 3. Assignment score vs final score
plt.figure()
plt.scatter(df["assignment_score"], df["final_score"])
plt.xlabel("Assignment Score")
plt.ylabel("Final Score")
plt.title("Assignment Score vs Final Score")
plt.show()

# 4. Attendance vs final score
plt.figure()
plt.scatter(df["attendance"], df["final_score"])
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.title("Attendance vs Final Score")
plt.show()