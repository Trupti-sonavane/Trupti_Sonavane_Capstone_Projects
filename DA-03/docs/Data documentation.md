\# Data Documentation

\##Retail \& Supply Chain Control Tower



\## 1. Overview



This document describes the datasets used in the Nexvia Retail \& Supply Chain Control Tower project.



The project uses Python-generated simulated data to analyze inventory levels, supplier information, shipment performance, and product demand.



The generated datasets are stored in CSV format and imported into PostgreSQL for data analysis and dashboard development.



\## 2. Data Sources



The project uses four CSV datasets generated through the Python script `generate\_data.py`.



| Dataset | CSV File | Number of Records |

|---|---|---:|

| Inventory | `inventory.csv` | 100 |

| Suppliers | `suppliers.csv` | 10 |

| Shipments | `shipments.csv` | 200 |

| Product Demand | `product\_demand.csv` | 9,000 |

| \*\*Total\*\* | \*\*4 CSV files\*\* | \*\*9,310\*\* |



\*\*Data Source:\*\* Synthetically generated data using Python.



\## 3. Dataset Details



\### 3.1 Inventory Dataset



\*\*File:\*\* `inventory.csv`



\*\*Purpose:\*\* Maintains product-level inventory information and supports stock monitoring and low-stock identification.



| Column Name | Data Type | Description |

|---|---|---|

| `product\_id` | String | Unique identifier of the product |

| `product\_name` | String | Name of the product |

| `warehouse\_id` | String | Identifier of the warehouse |

| `stock\_quantity` | Integer | Available stock quantity |

| `reorder\_level` | Integer | Minimum stock level for replenishment |

| `last\_updated` | ISO Datetime | Date and time of the last update |



\*\*Total Records:\*\* 100



\### 3.2 Suppliers Dataset



\*\*File:\*\* `suppliers.csv`



\*\*Purpose:\*\* Stores supplier details and performance-related information for supplier analysis.



| Column Name | Data Type | Description |

|---|---|---|

| `supplier\_id` | String | Unique supplier identifier |

| `supplier\_name` | String | Name of the supplier |

| `contact\_email` | String | Supplier contact email |

| `lead\_time\_days` | Integer | Expected supplier lead time in days |

| `reliability\_score` | Float | Supplier reliability score |



\*\*Total Records:\*\* 10



\### 3.3 Shipments Dataset



\*\*File:\*\* `shipments.csv`



\*\*Purpose:\*\* Tracks shipment details and helps identify delayed deliveries and shipment performance.



| Column Name | Data Type | Description |

|---|---|---|

| `shipment\_id` | String | Unique shipment identifier |

| `supplier\_id` | String | Associated supplier identifier |

| `product\_id` | String | Associated product identifier |

| `order\_date` | ISO Date | Date when the shipment was ordered |

| `expected\_delivery\_date` | ISO Date | Expected delivery date |

| `actual\_delivery\_date` | ISO Date | Actual delivery date |

| `shipment\_status` | String | Current shipment status |

| `quantity` | Integer | Quantity of products in the shipment |



\*\*Total Records:\*\* 200



\### 3.4 Product Demand Dataset



\*\*File:\*\* `product\_demand.csv`



\*\*Purpose:\*\* Contains historical product demand information used for demand analysis and forecasting.



| Column Name | Data Type | Description |

|---|---|---|

| `demand\_date` | ISO Date | Date of recorded product demand |

| `product\_id` | String | Associated product identifier |

| `units\_sold` | Integer | Number of units sold |



\*\*Total Records:\*\* 9,000



\## 4. Data Relationships



The datasets are connected using common identifiers.



| Primary Dataset | Related Dataset | Common Column |

|---|---|---|

| Inventory | Shipments | `product\_id` |

| Inventory | Product Demand | `product\_id` |

| Suppliers | Shipments | `supplier\_id` |



These relationships support integrated analysis of stock availability, supplier performance, shipment delays, and product demand.



\## 5. Data Storage and Database Structure



The generated CSV files are imported into PostgreSQL.



\*\*Database:\*\* PostgreSQL



\*\*Database Tables:\*\*



\- `inventory`

\- `suppliers`

\- `shipments`

\- `product\_demand`



The PostgreSQL `inventory` table also contains an additional `inventory\_id` integer column generated at the database level. This column is not part of the original CSV dataset.



\## 6. Data Generation and Import Process



The data pipeline follows these steps:



1\. Python generates simulated supply chain datasets.

2\. Four CSV files are created.

3\. The CSV files are imported into PostgreSQL.

4\. The imported data is used for SQL analysis and dashboard reporting.

5\. The hourly automation process regenerates and imports updated datasets.



\*\*Python Scripts:\*\*



\- `generate\_data.py` – Generates the datasets.

\- `import\_to\_postgres.py` – Imports CSV data into PostgreSQL.

\- `hourly\_refresh.py` – Automates dataset generation and database import.



\## 7. Data Usage in the Project



| Dataset | Application |

|---|---|

| Inventory | Inventory monitoring and low-stock identification |

| Suppliers | Supplier performance analysis |

| Shipments | Shipment tracking and delay analysis |

| Product Demand | Demand analysis and forecasting |



\## 8. Data Quality and Validation



The data pipeline validates successful dataset generation and PostgreSQL import through execution results and logs.



The successful import results confirmed:



\- 100 inventory records imported.

\- 10 supplier records imported.

\- 200 shipment records imported.

\- 9,000 product demand records imported.



\*\*Total records imported: 9,310.\*\*



\## 9. Conclusion



The four datasets provide the foundation for the Retail \& Supply Chain Control Tower project.



Their integration in PostgreSQL enables centralized data analysis and supports inventory monitoring, supplier evaluation, shipment delay analysis, demand forecasting, and dashboard-based decision-making.

