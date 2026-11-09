from pathlib import Path
import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

PROJECT_DIR = Path(__file__).resolve().parent.parent

connection_url = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password=os.getenv("POSTGRES_PASSWORD"),
    host="localhost",
    port=5432,
    database="retail_supply_chain",
)

if not os.getenv("POSTGRES_PASSWORD"):
    raise ValueError("POSTGRES_PASSWORD is not set.")

engine = create_engine(connection_url)

files = {
    "suppliers": "suppliers.csv",
    "inventory": "inventory.csv",
    "shipments": "shipments.csv",
    "product_demand": "product_demand.csv",
}

try:
    data = {
        table: pd.read_csv(PROJECT_DIR / filename)
        for table, filename in files.items()
    }

    with engine.begin() as conn:
        # Delete in reverse dependency order
        for table in ["product_demand", "shipments", "inventory", "suppliers"]:
            conn.execute(text(f"DELETE FROM public.{table}"))

        # Insert in dependency order
        for table, df in data.items():
            df.to_sql(
                table,
                conn,
                schema="public",
                if_exists="append",
                index=False,
                method="multi",
                chunksize=1000,
            )
            print(f"{table}: {len(df)} rows imported.")

    print("All CSV data imported successfully.")

finally:
    engine.dispose()