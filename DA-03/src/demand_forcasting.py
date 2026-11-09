import pandas as pd
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Locate project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "product_demand.csv"

# Load demand data
df = pd.read_csv(DATA_FILE)
df["demand_date"] = pd.to_datetime(df["demand_date"])

# Select one product for forecasting
product_id = "P001"
product_df = df[df["product_id"] == product_id].copy()

# Aggregate demand by date
daily_demand = (
    product_df.groupby("demand_date")["units_sold"]
    .sum()
    .reset_index()
    .sort_values("demand_date")
)

# Create a numeric time feature
daily_demand["day_number"] = (
    daily_demand["demand_date"] - daily_demand["demand_date"].min()
).dt.days

X = daily_demand[["day_number"]]
y = daily_demand["units_sold"]

# Use the last 14 days for testing
if len(daily_demand) <= 14:
    raise ValueError("Not enough daily records for forecasting.")

X_train = X.iloc[:-14]
X_test = X.iloc[-14:]
y_train = y.iloc[:-14]
y_test = y.iloc[-14:]

# Train a simple forecasting model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate on the last 14 days
predictions = model.predict(X_test)
predictions = np.maximum(predictions, 0)

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("DEMAND FORECASTING RESULTS")
print("-" * 35)
print(f"Product: {product_id}")
print(f"Daily records: {len(daily_demand)}")
print(f"Test period: 14 days")
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")

# Train on all available data and forecast the next 7 days
model.fit(X, y)

last_day = int(X["day_number"].max())
future_days = pd.DataFrame({
    "day_number": range(last_day + 1, last_day + 8)
})

future_predictions = np.maximum(
    model.predict(future_days[["day_number"]]), 0
)

future_dates = pd.date_range(
    daily_demand["demand_date"].max() + pd.Timedelta(days=1),
    periods=7
)

forecast_df = pd.DataFrame({
    "forecast_date": future_dates,
    "product_id": product_id,
    "forecast_units": np.round(future_predictions, 2)
})

output_file = PROJECT_DIR / "demand_forecast.csv"
forecast_df.to_csv(output_file, index=False)

print("\nNext 7 days forecast:")
print(forecast_df.to_string(index=False))
print(f"\nForecast saved to: {output_file}")