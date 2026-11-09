SELECT
    COUNT(*) AS total_shipments,
    SUM(
        CASE
            WHEN shipment_status = 'On Time' THEN 1
            ELSE 0
        END
    ) AS on_time_shipments,
    SUM(
        CASE
            WHEN shipment_status = 'Delayed' THEN 1
            ELSE 0
        END
    ) AS delayed_shipments,
    ROUND(
        100.0 * SUM(
            CASE
                WHEN shipment_status = 'On Time' THEN 1
                ELSE 0
            END
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS on_time_delivery_rate_pct
FROM shipments;