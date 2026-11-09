\# Retail and Supply Chain Control Tower



\## 1. Project Overview



The Retail and Supply Chain Control Tower is a data analytics

project designed to monitor inventory levels, supplier performance,

shipment deliveries, and product demand.



The project uses a PostgreSQL database to store and analyze

supply chain data. SQL is used to calculate key performance

indicators (KPIs), identify inventory risks, and monitor

delivery performance.



Python will be used for anomaly detection and demand forecasting.

A dashboard will present important metrics and insights to

support data-driven business decisions.



\## 2. Problem Statement



Retail businesses may face inventory shortages, excess stock,

delayed shipments, unreliable suppliers, and changes in product

demand.



Without centralized monitoring, these issues can affect product

availability, delivery performance, and operational efficiency.



This project aims to develop a centralized monitoring solution

to analyze supply chain data and identify potential risks.



\## 3. Project Objectives



\- Monitor product inventory and stock availability.

\- Identify products that are out of stock or below reorder levels.

\- Measure supplier lead times and delivery performance.

\- Analyze shipment delays.

\- Calculate important supply chain KPIs.

\- Detect unusual inventory and demand patterns.

\- Forecast future product demand.

\- Present insights through a dashboard.

\- Support better inventory and replenishment decisions.



\## 4. Dataset Description



The project uses simulated supply chain data generated with Python.



The dataset contains four CSV files:



| Dataset | Description | Expected Records |

|---|---|---:|

| inventory.csv | Product stock and reorder levels | 100 |

| suppliers.csv | Supplier details and lead times | 10 |

| shipments.csv | Shipment and delivery information | 200 |

| product\_demand.csv | Daily product demand | 9000 |



Note: Actual database record counts will be verified during

data validation.



\## 5. Technology Stack



\- Python: Dataset generation, anomaly detection, forecasting

\- PostgreSQL: Database storage and SQL analysis

\- SQL: KPI calculations and data validation

\- Apache Superset: Planned dashboard development

\- GitHub: Version control and project documentation



\## 6. Project Status



\- Simulated dataset generation: Completed

\- PostgreSQL database setup: Completed

\- CSV data import: Completed

\- KPI development: In progress

\- Anomaly detection: Planned

\- Demand forecasting: Planned

\- Dashboard development: Planned

\- Testing and documentation: In progress



\## 7. SQL Analysis and KPI Development



PostgreSQL is used to analyze inventory, supplier, shipment,

and product demand data.



The following KPIs have been developed:



\### Inventory KPIs

\- Total products are counted from the inventory table.

\- Out-of-stock products are identified using stock quantity = 0.

\- Low-stock products are identified when stock quantity is

&#x20; less than or equal to the reorder level.

\- Days of inventory is estimated using current stock divided

&#x20; by average daily product demand.



\### Supplier KPIs

\- Total number of suppliers.

\- Average supplier lead time in days.

\- Average supplier reliability score.



\### Shipment KPIs

\- Total shipments.

\- Number of on-time shipments.

\- Number of delayed shipments.

\- On-time delivery rate.

\- Average delivery delay in days.

\- Maximum delivery delay in days.



\### Demand Analysis

Daily product demand is aggregated by product to calculate

average daily demand. This value is used to estimate how many

days the current inventory may last.



\### Data Validation Notes

\- The generated inventory CSV contains 100 product records.

\- The PostgreSQL inventory table currently contains 110 records.

\- The product demand dataset contains 9,000 records.

\- The Days of Inventory analysis joins inventory with demand

&#x20; data, so only products with matching demand records are included.

\- The inventory record-count difference will be investigated

&#x20; before finalizing the project.



\## 8. Initial KPI Results



The following KPI results were obtained from PostgreSQL

during the initial analysis of the simulated dataset.



| KPI | Initial Result |

|---|---:|

| Total inventory records | 110 |

| Out-of-stock products | 0 |

| Low-stock products | 24 |

| Total suppliers | 10 |

| Average supplier lead time | 9.50 days |

| Total shipments | 200 |

| On-time delivery rate | 26.50% |



\### Initial Observations



\- No products were identified with zero stock in the current

&#x20; inventory data.

\- 24 inventory records are at or below their reorder levels.

\- The average supplier lead time is 9.50 days.

\- The initial on-time delivery rate is 26.50%, indicating

&#x20; that delivery performance needs further investigation.



\### Validation Notes



\- Inventory contains 110 records, while the generated

&#x20; inventory CSV contains 100 records.

\- The reason for this difference needs investigation.

\- Shipment delivery performance will be validated against

&#x20; expected and actual delivery dates.

\- These are initial results and may be updated after

&#x20; data validation.



\## 9. Delivery Delay Analysis



Shipment delivery performance was analyzed using the

expected and actual delivery dates stored in PostgreSQL.



| KPI | Result |

|---|---:|

| Total Shipments | 200 |

| Delayed Shipments | 147 |

| Delayed Shipment Rate | 73.50% |

| Average Delivery Delay | 4.53 days |

| Maximum Delivery Delay | 8 days |



\### Key Insight



The analysis identified 147 delayed shipments out of 200

shipments, representing a delay rate of 73.50%.



The average delivery delay among delayed shipments was

4.53 days, while the maximum delay was 8 days.



These results highlight a potential delivery performance

issue that should be investigated further.



\## 10. Days of Inventory Analysis



Days of Inventory estimates how long the current stock

may last based on average daily product demand.



The calculation uses the following formula:



Days of Inventory = Current Stock Quantity / Average Daily Demand



\### Results



| KPI | Result |

|---|---:|

| Products Analyzed | 100 |

| Average Days of Inventory | 6.27 days |

| Minimum Days of Inventory | 0.06 days |

| Maximum Days of Inventory | 12.80 days |



\### Key Insights



\- The average inventory coverage is approximately 6.27 days.

\- Some products have very low inventory coverage, indicating

&#x20; potential stock-out risks.

\- Products with higher inventory coverage may have more stock

&#x20; available relative to their average demand.



\### Business Recommendation



Prioritize products with low inventory coverage for

replenishment review. Consider both current stock levels

and demand patterns before making replenishment decisions.



Note: These estimates are based on simulated inventory

and demand data. Actual demand may vary.



\## 11. Demand Anomaly Detection



Python and pandas are used to identify unusual demand values

using the Z-score statistical method.



\### Methodology



\- Calculate the mean and standard deviation of units sold.

\- Calculate the Z-score for each demand record.

\- Flag records where the absolute Z-score is greater than 2.

\- Save the analysis results to anomaly\_results.csv.



\### Initial Results



\### Initial Results



| Metric | Initial Method | Product-wise Method |

|---|---|---|

| Method | Global Z-score | Product-wise Z-score |

| Anomaly threshold | Absolute Z-score > 2 | Absolute Z-score > 2 |

| Anomalies detected | 0 | 5 |



\### Key Findings



\- The initial global analysis detected no anomalies.

\- The improved product-wise analysis detected 5 unusual

&#x20; demand records.

\- Each product's demand is evaluated relative to its own

&#x20; average demand and standard deviation.

\- The detected records should be reviewed before making

&#x20; inventory or replenishment decisions.



\### Output Files



\- anomaly\_results\_v2.csv: Complete demand dataset with

&#x20; product-wise Z-scores and anomaly flags.

\- detected\_anomalies\_v2.csv: Records flagged as anomalies.



Note: The data is simulated. Detected anomalies are

statistical outliers and do not automatically indicate

actual business problems.



\## 12. Demand Forecasting



Python and Scikit-learn are used to forecast product demand

based on historical daily sales data.



\### Methodology



\- Historical demand data is loaded from product\_demand.csv.

\- Product P001 is selected for the initial forecasting model.

\- Linear Regression is used to model the demand trend.

\- The last 14 days are reserved for model evaluation.

\- The model is evaluated using Mean Absolute Error (MAE)

&#x20; and Root Mean Squared Error (RMSE).

\- After evaluation, the model is trained on all available

&#x20; records to forecast demand for the next 7 days.



\### Model Evaluation Results



| Metric | Result |

|---|---:|

| Product analyzed | P001 |

| Test period | 14 days |

| MAE | 8.18 units |

| RMSE | 9.28 units |

| Forecast horizon | 7 days |



\### Interpretation



The model's Mean Absolute Error is 8.18 units, meaning

that the average absolute difference between predicted

and actual demand during the test period was 8.18 units.



The RMSE is 9.28 units and gives greater weight to larger

prediction errors.



These metrics should be compared with a simple baseline

forecast before deciding whether the model is suitable

for business use.



\### Output File



\- demand\_forecast.csv: Contains the forecast dates,

&#x20; product ID, and predicted demand for the next 7 days.



Note: This is an initial forecasting model trained on

simulated demand data. Results are not validated against

real business demand.



\## 13. Forecast Model Comparison and Evaluation



The Linear Regression forecasting model was compared with

a simple baseline model that predicts the average demand

observed in the training dataset.



Both models were evaluated on the same 14-day test period

for product P001.



\### Comparison Results



| Model | MAE | RMSE |

|---|---:|---:|

| Baseline Average | 8.14 | 9.21 |

| Linear Regression | 8.18 | 9.28 |



\### Findings



\- The Baseline Average model achieved an MAE of 8.14 units

&#x20; and an RMSE of 9.21 units.

\- Linear Regression achieved an MAE of 8.18 units and an

&#x20; RMSE of 9.28 units.

\- The baseline model performed slightly better on both

&#x20; evaluation metrics.

\- Linear Regression has not demonstrated an improvement

&#x20; over the baseline in this initial experiment.



\### Conclusion



The baseline model is the better-performing option among

these two models for the current test period.



Further experimentation with time-series methods, additional

historical data, and demand patterns is recommended before

selecting a production forecasting model.



Note: Evaluation uses simulated data for product P001

and a 14-day holdout period. Results may differ on other

products or datasets.



\## 14. Automated Supply Chain Alert Generation



A Python-based alert generation script was developed to identify low-stock inventory items and delayed shipments using the simulated project datasets.



\### Alert Rules



\- \*\*Low Stock Alert:\*\* Generated when stock quantity is less than or equal to the reorder level.

\- \*\*Delayed Shipment Alert:\*\* Generated when the actual delivery date is later than the expected delivery date.

\- \*\*Severity:\*\* Low-stock alerts are classified as HIGH. Shipment delays of five days or more are classified as HIGH; shorter delays are classified as MEDIUM.



\### Results



| Alert Type | Alerts Generated |

|---|---:|

| Delayed Shipment | 147 |

| Low Stock | 19 |

| \*\*Total\*\* | \*\*166\*\* |



\### Output



The script saves the generated alerts to `supply\_chain\_alerts.csv` in the project root folder. Each record contains the alert type, item identifier, message, and severity.



\### Limitations



Alerts are generated when the Python script is executed. Automated hourly scheduling and real-time notifications have not yet been implemented. Results are based on simulated datasets.



\## 15. Automated Testing and Validation



Six automated tests were implemented in `src/test\_alerts.py` to validate the generated supply chain alert report.



\### Test Cases



1\. Verify that the alerts CSV file exists.

2\. Verify that all required columns are present.

3\. Verify that the alert report is not empty.

4\. Verify that alert types contain only supported values.

5\. Verify that alert severity values are valid.

6\. Verify that alert messages are not empty.



\### Test Results



\- Total tests executed: 6

\- Tests passed: 6

\- Tests failed: 0

\- Overall result: PASS



\### Execution



The tests were executed using:



`python test\_alerts.py`



All six tests passed against the generated simulated-data alert report.



Note: These tests validate the alert output file and its contents. They do not yet test database connectivity, hourly refresh, or end-to-end system performance.

# Hourly Automated Data Refresh

## 1. Overview

The Retail & Supply Chain Control Tower project implements an automated hourly data refresh pipeline using Python, CSV files, PostgreSQL, and Windows Task Scheduler.

The automation generates updated supply chain datasets and imports them into PostgreSQL automatically every hour without requiring manual execution.

## 2. Technology Used

- Python 3.13
- PostgreSQL
- CSV files
- Windows Task Scheduler
- Windows Batch Script (.bat)

## 3. Automation Workflow

1. Windows Task Scheduler triggers the refresh process every hour.
2. The `run_refresh.bat` file starts the Python automation script.
3. The `hourly_refresh.py` script executes `generate_data.py`.
4. Updated CSV datasets are generated.
5. The script executes `import_to_postgres.py`.
6. CSV data is imported into PostgreSQL tables.
7. Execution details and errors are recorded in `hourly_refresh.log`.

## 4. Python Automation Script

File: `src/hourly_refresh.py`

The script automates two major operations:

- Dataset generation using `generate_data.py`.
- PostgreSQL data import using `import_to_postgres.py`.

The process completes successfully only when both operations execute without errors.

## 5. Batch File Configuration

File: `run_refresh.bat`

The batch file:
- Navigates to the project directory.
- Executes the Python automation script.
- Redirects execution output to `hourly_refresh.log`.
- Records the process exit code.

## 6. Windows Task Scheduler Configuration

Task Name: `Retail Supply Chain Hourly Refresh`

Configuration:
- Trigger: Daily
- Repeat interval: Every 1 hour
- Repeat duration: Indefinitely
- Action: Execute `run_refresh.bat` through Windows Command Prompt.
- Task Status: Enabled

This configuration allows the data refresh pipeline to run automatically every hour.

## 7. PostgreSQL Data Import Results

The automation successfully generated and imported the following records:

| Dataset | Imported Records |
|---|---:|
| Suppliers | 10 |
| Inventory | 100 |
| Shipments | 200 |
| Product Demand | 9,000 |
| **Total** | **9,310** |

All four datasets were imported successfully into PostgreSQL.

## 8. Execution Logging

The file `hourly_refresh.log` stores:
- Refresh start time.
- Dataset generation output.
- PostgreSQL import results.
- Process completion time.
- Exit code.

A successful execution returns exit code `0`.

## 9. Testing and Validation

The automation was manually executed and tested.

The following results confirmed successful execution:

- Dataset generation completed successfully.
- All four datasets were imported into PostgreSQL.
- Hourly Task Scheduler configuration was enabled.
- Last Run Result was `0`.
- Execution logs confirmed successful refresh operations.

## 10. Dashboard Refresh Note

The Python automation updates PostgreSQL data hourly.

The Apache Superset dashboard is a separate presentation layer. Its dashboard auto-refresh configuration must be completed separately. Therefore, hourly database updates do not by themselves confirm that the dashboard visualizations are automatically refreshing.

## 11. Conclusion

The hourly automated refresh pipeline reduces manual data-loading effort and maintains updated supply chain datasets in PostgreSQL. It provides a repeatable data preparation and ingestion workflow for the Retail & Supply Chain Control Tower project.

Note: The dataset is simulated and the results represent

the generated data, not real business operations.

