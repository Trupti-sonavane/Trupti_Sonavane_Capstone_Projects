SELECT
    COUNT(*) AS delayed_shipments,
    ROUND(
        AVG(actual_delivery_date - expected_delivery_date)
            FILTER (WHERE shipment_status = 'Delayed'),
        2
    ) AS avg_delay_days,
    MAX(actual_delivery_date - expected_delivery_date)
        FILTER (WHERE shipment_status = 'Delayed')
        AS max_delay_days
FROM shipments;