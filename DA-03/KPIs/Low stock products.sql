SELECT
    COUNT(*) AS total_products,
    SUM(
        CASE
            WHEN stock_quantity <= reorder_level THEN 1
            ELSE 0
        END
    ) AS low_stock_products
FROM inventory;