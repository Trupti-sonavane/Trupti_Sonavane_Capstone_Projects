from pathlib import Path
import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

PROJECT_DIR = Path(__file__).resolve().parent.parent

# Load demand data
df = pd.read_csv(PROJECT_DIR / "product_demand.csv")
df["demand_date"] = pd.to_datetime(df["demand_date"])

# Select product P001
product_df = df[df["product_id"] == "P001"].copy()

# Prepare Prophet format
prophet_df = product_df[["demand_date", "units_sold"]].rename(
    columns={"demand_date": "ds", "units_sold": "y"}
).sort_values("ds")

# Train-test split: last 14 days for testing
train = prophet_df.iloc[:-14]
test = prophet_df.iloc[-14:]

# Train Prophet model
model = Prophet()
model.fit(train)

# Evaluate model
test_future = test[["ds"]]
predictions = model.predict(test_future)

mae = mean_absolute_error(test["y"], predictions["yhat"])
rmse = np.sqrt(mean_squared_error(test["y"], predictions["yhat"]))

print("Prophet Model Evaluation")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))

# Train final model on complete data
final_model = Prophet()
final_model.fit(prophet_df)

# Forecast next 7 days
future = final_model.make_future_dataframe(periods=7)
forecast = final_model.predict(future)

# Save forecast
forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(7).to_csv(
    PROJECT_DIR / "prophet_forecast.csv",
    index=False
)

print("7-day Prophet forecast saved successfully.")