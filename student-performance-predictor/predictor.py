# Student Performance Predictor

print("Student Performance Predictor")
print("-----------------------------")

name = input("Enter student name: ")

# Get valid study hours
while True:
    try:
        study_hours = float(input("Enter study hours per day: "))

        if study_hours < 0 or study_hours > 24:
            print("Please enter study hours between 0 and 24.")
        else:
            break

    except ValueError:
        print("Please enter a valid number.")

# Get valid attendance
while True:
    try:
        attendance = float(input("Enter attendance percentage: "))

        if attendance < 0 or attendance > 100:
            print("Please enter attendance between 0 and 100.")
        else:
            break

    except ValueError:
        print("Please enter a valid number.")

# Convert study hours into a score out of 100
study_score = min(study_hours * 10, 100)

# Calculate estimated performance
performance_score = (study_score * 0.60) + (attendance * 0.40)

print("\nStudent Details")
print("Name:", name)
print("Study Hours:", study_hours)
print("Attendance:", attendance)

print("\nPredicted Performance Score:", round(performance_score, 2))

if performance_score >= 75:
    print("Performance Level: Excellent")
elif performance_score >= 50:
    print("Performance Level: Good")
else:
    print("Performance Level: Needs Improvement")