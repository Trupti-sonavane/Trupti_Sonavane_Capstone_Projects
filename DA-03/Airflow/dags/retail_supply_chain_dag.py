from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def run_pipeline():
    print("Retail & Supply Chain pipeline started successfully.")
    print("Hourly pipeline execution test completed.")


with DAG(
    dag_id="retail_supply_chain_hourly_pipeline",
    start_date=datetime(2026, 10, 31),
    schedule="0 * * * *",
    catchup=False,
    tags=["retail", "supply-chain"],
) as dag:

    pipeline_task = PythonOperator(
        task_id="run_pipeline",
        python_callable=run_pipeline,
    )