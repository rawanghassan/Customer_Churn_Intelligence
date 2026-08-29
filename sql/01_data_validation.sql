-- =====================================================
-- Project: Customer Churn Intelligence
-- File: 01_data_validation.sql
-- Purpose: Validate and inspect the raw customer data
-- =====================================================


-- 1. Preview the first 10 customer records

SELECT *
FROM public.telco_customer_churn_raw
LIMIT 10;


-- 2. Check the total number of records
-- and the number of unique customers

SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM public.telco_customer_churn_raw;


-- 3. Check for duplicate customer IDs

SELECT
    customer_id,
    COUNT(*) AS duplicate_count
FROM public.telco_customer_churn_raw
GROUP BY customer_id
HAVING COUNT(*) > 1;


-- 4. Review customer churn distribution

SELECT
    churn_label,
    COUNT(*) AS customer_count,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (),
        2
    ) AS percentage
FROM public.telco_customer_churn_raw
GROUP BY churn_label
ORDER BY customer_count DESC;