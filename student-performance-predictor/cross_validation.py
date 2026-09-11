import pandas as pd
from pathlib import Path

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score, mean_absolute_error

# Load the dataset
data_path = Path(__file__).parent / "data" / "students.csv"
data = pd.read_csv(data_path)

# Features and target
X = data[[
    "study_hours",
    "attendance",
    "previous_score",
    "assignment_score"
]]

y = data["final_score"]

# Create 5 folds
kf = KFold(n_splits=5, shuffle=True, random_state=42)

r2_scores = []
mae_scores = []

# Perform cross-validation
for train_index, test_index in kf.split(X):

    X_train = X.iloc[train_index]
    X_test = X.iloc[test_index]

    y_train = y.iloc[train_index]
    y_test = y.iloc[test_index]

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Keep predictions between 0 and 100
    predictions = predictions.clip(0, 100)

    # Calculate metrics
    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)

    r2_scores.append(r2)
    mae_scores.append(mae)


# Display results
print("Final Model - 5-Fold Cross-Validation")
print("--------------------------------------")

for i in range(5):
    print(
        f"Fold {i + 1}: "
        f"R² = {r2_scores[i]:.3f} | "
        f"MAE = {mae_scores[i]:.3f}"
    )

print("\nAverage R²:", round(sum(r2_scores) / 5, 3))
print("Average MAE:", round(sum(mae_scores) / 5, 3))

print("\nR² Standard Deviation:", round(pd.Series(r2_scores).std(), 3))
print("MAE Standard Deviation:", round(pd.Series(mae_scores).std(), 3))