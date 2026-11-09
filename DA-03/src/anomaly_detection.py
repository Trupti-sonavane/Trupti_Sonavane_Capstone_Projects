import pandas as pd
from pathlib import Path

# Locate project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "product_demand.csv"

# Load demand data
df = pd.read_csv(DATA_FILE)

# Calculate Z-score separately for each product
product_groups = df.groupby("product_id")["units_sold"]

df["product_mean"] = product_groups.transform("mean")
df["product_std"] = product_groups.transform("std")

# Avoid division by zero
df["z_score"] = (
    (df["units_sold"] - df["product_mean"])
    / df["product_std"].replace(0, float("nan"))
)

# Flag unusual demand values
df["is_anomaly"] = df["z_score"].abs() > 2

# Collect anomaly records
anomalies = df[df["is_anomaly"]].copy()

# Display results
print("PRODUCT-WISE ANOMALY DETECTION")
print("-" * 40)
print(f"Total demand records: {len(df)}")
print(f"Unique products: {df['product_id'].nunique()}")
print(f"Anomalies detected: {len(anomalies)}")

# Save complete results
output_file = PROJECT_DIR / "anomaly_results_v2.csv"
df.to_csv(output_file, index=False)

# Save only anomaly records separately
anomaly_file = PROJECT_DIR / "detected_anomalies_v2.csv"
anomalies.to_csv(anomaly_file, index=False)

print(f"All results saved to: {output_file}")
print(f"Anomaly records saved to: {anomaly_file}")