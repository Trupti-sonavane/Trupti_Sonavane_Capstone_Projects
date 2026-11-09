import csv
import random
from datetime import date, datetime, timedelta
from pathlib import Path

random.seed(42)

OUTPUT_DIR = Path(__file__).resolve().parent

# 1. INVENTORY DATA
products = []

product_names = [
    "Headphones", "Wireless Mouse", "Keyboard", "USB Cable",
    "Monitor", "Laptop Stand", "Webcam", "Bluetooth Speaker",
    "Power Bank", "Gaming Mouse"
]

for i in range(1, 101):
    stock = random.randint(0, 200)
    reorder_level = random.randint(10, 50)

    products.append({
        "product_id": f"P{i:03}",
        "product_name": product_names[(i - 1) % len(product_names)],
        "warehouse_id": f"WH{random.randint(1, 4):02}",
        "stock_quantity": stock,
        "reorder_level": reorder_level,
        "last_updated": datetime.now().isoformat(timespec="seconds")
    })

with open(OUTPUT_DIR / "inventory.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=products[0].keys())
    writer.writeheader()
    writer.writerows(products)


# 2. SUPPLIER DATA
suppliers = []

for i in range(1, 11):
    suppliers.append({
        "supplier_id": f"S{i:03}",
        "supplier_name": f"Supplier {i}",
        "lead_time_days": random.randint(2, 14),
        "reliability_score": round(random.uniform(0.75, 0.99), 2),
        "contact_email": f"supplier{i}@example.com"
    })

with open(OUTPUT_DIR / "suppliers.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=suppliers[0].keys())
    writer.writeheader()
    writer.writerows(suppliers)


# 3. SHIPMENT DATA
shipments = []
today = date.today()

for i in range(1, 201):
    supplier = random.choice(suppliers)
    order_date = today - timedelta(days=random.randint(1, 90))
    expected_days = supplier["lead_time_days"]
    actual_days = max(1, expected_days + random.randint(-2, 8))

    expected_date = order_date + timedelta(days=expected_days)
    actual_date = order_date + timedelta(days=actual_days)

    shipments.append({
        "shipment_id": f"SH{i:04}",
        "supplier_id": supplier["supplier_id"],
        "product_id": random.choice(products)["product_id"],
        "order_date": order_date.isoformat(),
        "expected_delivery_date": expected_date.isoformat(),
        "actual_delivery_date": actual_date.isoformat(),
        "shipment_status": (
            "Delayed" if actual_days > expected_days else "On Time"
        ),
        "quantity": random.randint(10, 500)
    })

with open(OUTPUT_DIR / "shipments.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=shipments[0].keys())
    writer.writeheader()
    writer.writerows(shipments)


# 4. DAILY PRODUCT DEMAND
demand_records = []

for day_offset in range(90):
    demand_date = today - timedelta(days=89 - day_offset)

    for product in products:
        demand_records.append({
            "demand_date": demand_date.isoformat(),
            "product_id": product["product_id"],
            "units_sold": random.randint(0, 30)
        })

with open(
    OUTPUT_DIR / "product_demand.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:
    writer = csv.DictWriter(file, fieldnames=demand_records[0].keys())
    writer.writeheader()
    writer.writerows(demand_records)

print("Dataset generation completed successfully!")
print(f"Inventory records: {len(products)}")
print(f"Supplier records: {len(suppliers)}")
print(f"Shipment records: {len(shipments)}")
print(f"Product demand records: {len(demand_records)}")
print(f"CSV files saved in: {OUTPUT_DIR}")