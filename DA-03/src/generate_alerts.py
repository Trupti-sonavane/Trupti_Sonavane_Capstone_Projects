from pathlib import Path
import pandas as pd

# Project folder path
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Input files
inventory_file = PROJECT_DIR / "inventory.csv"
shipments_file = PROJECT_DIR / "shipments.csv"

alerts = []

# Check inventory levels
inventory = pd.read_csv(inventory_file)

for _, row in inventory.iterrows():
    stock = row["stock_quantity"]
    reorder = row["reorder_level"]
    product = row["product_id"]

    if stock <= reorder:
        alerts.append({
            "alert_type": "LOW_STOCK",
            "item_id": product,
            "message": (
                f"Product {product} has low stock. "
                f"Current stock: {stock}, reorder level: {reorder}."
            ),
            "severity": "HIGH"
        })

# Check delayed shipments
shipments = pd.read_csv(shipments_file)

for _, row in shipments.iterrows():
    expected = pd.to_datetime(
        row["expected_delivery_date"], errors="coerce"
    )
    actual = pd.to_datetime(
        row["actual_delivery_date"], errors="coerce"
    )

    if pd.notna(expected) and pd.notna(actual) and actual > expected:
        delay_days = (actual - expected).days

        alerts.append({
            "alert_type": "DELAYED_SHIPMENT",
            "item_id": row["shipment_id"],
            "message": (
                f"Shipment {row['shipment_id']} is delayed "
                f"by {delay_days} days."
            ),
            "severity": "HIGH" if delay_days >= 5 else "MEDIUM"
        })

# Save alerts
alerts_df = pd.DataFrame(
    alerts,
    columns=["alert_type", "item_id", "message", "severity"]
)

output_file = PROJECT_DIR / "supply_chain_alerts.csv"
alerts_df.to_csv(output_file, index=False)

print("Alert generation completed!")
print(f"Total alerts generated: {len(alerts_df)}")
print(f"Alerts saved to: {output_file}")

if not alerts_df.empty:
    print("\nAlert summary:")
    print(alerts_df["alert_type"].value_counts())
    print("\nFirst 10 alerts:")
    print(alerts_df.head(10).to_string(index=False))
else:
    print("No alerts detected.")