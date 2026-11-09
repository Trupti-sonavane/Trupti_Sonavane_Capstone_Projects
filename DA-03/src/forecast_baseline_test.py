import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression

# Locate project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "product_demand.csv"

# Load demand data
df = pd.read_csv(DATA_FILE)
df["demand_date"] = pd.to_datetime(df["demand_date"])

# Select product for testing
product_id = "P001"
product_df = df[df["product_id"] == product_id].copy()

# Aggregate daily demand
daily = (
    product_df.groupby("demand_date")["units_sold"]
    .sum()
    .reset_index()
    .sort_values("demand_date")
)

# Create time feature
daily["day_number"] = (
    daily["demand_date"] - daily["demand_date"].min()
).dt.days

# Reserve the last 14 days for testing
train = daily.iloc[:-14].copy()
test = daily.iloc[-14:].copy()

# Baseline: predict using average demand in training data
baseline_predictions = np.full(
    len(test), train["units_sold"].mean()
)

# Linear Regression model
model = LinearRegression()
model.fit(train[["day_number"]], train["units_sold"])

linear_predictions = np.maximum(
    model.predict(test[["day_number"]]), 0
)

# Calculate evaluation metrics
baseline_mae = mean_absolute_error(
    test["units_sold"], baseline_predictions
)
baseline_rmse = np.sqrt(
    mean_squared_error(test["units_sold"], baseline_predictions)
)

linear_mae = mean_absolute_error(
    test["units_sold"], linear_predictions
)
linear_rmse = np.sqrt(
    mean_squared_error(test["units_sold"], linear_predictions)
)

print("FORECAST BASELINE COMPARISON")
print("-" * 40)
print(f"Product: {product_id}")
print(f"Test period: {len(test)} days")
print("\nBaseline Model:")
print(f"MAE: {baseline_mae:.2f}")
print(f"RMSE: {baseline_rmse:.2f}")

print("\nLinear Regression Model:")
print(f"MAE: {linear_mae:.2f}")
print(f"RMSE: {linear_rmse:.2f}")

# Save comparison results
results = pd.DataFrame({
    "model": ["Baseline Average", "Linear Regression"],
    "MAE": [baseline_mae, linear_mae],
    "RMSE": [baseline_rmse, linear_rmse]
})

output_file = PROJECT_DIR / "forecast_model_comparison.csv"
results.to_csv(output_file, index=False)

print(f"\nComparison saved to: {output_file}")