SELECT
    COUNT(*) AS total_suppliers,
    ROUND(AVG(lead_time_days), 2) AS avg_supplier_lead_time_days,
    ROUND(AVG(reliability_score), 2) AS avg_supplier_reliability
FROM suppliers;