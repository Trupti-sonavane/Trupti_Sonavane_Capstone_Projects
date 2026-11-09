SELECT
    product_id,
    product_name,
    warehouse_id,
    stock_quantity,
    reorder_level,
    reorder_level - stock_quantity AS units_below_reorder
FROM inventory
WHERE stock_quantity <= reorder_level
ORDER BY units_below_reorder DESC;