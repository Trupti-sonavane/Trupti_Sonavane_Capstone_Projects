SELECT
    COUNT(*) AS total_products,
    SUM(CASE
        WHEN stock_quantity = 0 THEN 1
        ELSE 0
    END) AS out_of_stock_products,
    ROUND(
        100.0 * SUM(
            CASE WHEN stock_quantity = 0 THEN 1 ELSE 0 END
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS stock_out_rate_pct
FROM inventory;