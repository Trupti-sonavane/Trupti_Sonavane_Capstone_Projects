WITH demand_summary AS (
    SELECT
        product_id,
        AVG(units_sold) AS avg_daily_demand
    FROM product_demand
    GROUP BY product_id
),
inventory_days AS (
    SELECT
        i.product_id,
        i.stock_quantity,
        d.avg_daily_demand,
        CASE
            WHEN d.avg_daily_demand > 0
            THEN i.stock_quantity / d.avg_daily_demand
            ELSE NULL
        END AS days_of_inventory
    FROM inventory i
    JOIN demand_summary d
        ON i.product_id = d.product_id
)
SELECT
    COUNT(*) AS products_analyzed,
    ROUND(AVG(days_of_inventory), 2) AS avg_days_of_inventory,
    ROUND(MIN(days_of_inventory), 2) AS min_days_of_inventory,
    ROUND(MAX(days_of_inventory), 2) AS max_days_of_inventory
FROM inventory_days;