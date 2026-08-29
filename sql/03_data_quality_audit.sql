-- =====================================================
-- Project: Customer Churn Intelligence
-- File: 03_data_quality_audit.sql
-- Purpose: Audit the quality of the cleaned data
-- =====================================================


-- =====================================================
-- 1. Check row counts and missing values
-- =====================================================

SELECT

    COUNT(*) AS total_rows,

    COUNT(DISTINCT customer_id)
        AS unique_customers,

    COUNT(*) FILTER (
        WHERE customer_id IS NULL
        OR BTRIM(customer_id) = ''
    ) AS missing_customer_id,

    COUNT(*) FILTER (
        WHERE tenure_months IS NULL
    ) AS missing_tenure_months,

    COUNT(*) FILTER (
        WHERE monthly_charges IS NULL
    ) AS missing_monthly_charges,

    COUNT(*) FILTER (
        WHERE total_charges IS NULL
    ) AS missing_total_charges,

    COUNT(*) FILTER (
        WHERE churn_label IS NULL
    ) AS missing_churn_label,

    COUNT(*) FILTER (
        WHERE churn_value IS NULL
    ) AS missing_churn_value,

    COUNT(*) FILTER (
        WHERE churn_score IS NULL
    ) AS missing_churn_score,

    COUNT(*) FILTER (
        WHERE cltv IS NULL
    ) AS missing_cltv,

    COUNT(*) FILTER (
        WHERE churn_reason IS NULL
    ) AS missing_churn_reason

FROM public.telco_customer_churn_clean;



-- =====================================================
-- 2. Review numerical ranges
-- =====================================================

SELECT

    MIN(tenure_months)
        AS minimum_tenure,

    MAX(tenure_months)
        AS maximum_tenure,

    ROUND(
        AVG(tenure_months)::NUMERIC,
        2
    ) AS average_tenure,

    MIN(monthly_charges)
        AS minimum_monthly_charges,

    MAX(monthly_charges)
        AS maximum_monthly_charges,

    ROUND(
        AVG(monthly_charges),
        2
    ) AS average_monthly_charges,

    MIN(total_charges)
        AS minimum_total_charges,

    MAX(total_charges)
        AS maximum_total_charges,

    MIN(churn_score)
        AS minimum_churn_score,

    MAX(churn_score)
        AS maximum_churn_score,

    MIN(cltv)
        AS minimum_cltv,

    MAX(cltv)
        AS maximum_cltv

FROM public.telco_customer_churn_clean;



-- =====================================================
-- 3. Check invalid or negative numerical values
-- =====================================================

SELECT

    COUNT(*) FILTER (
        WHERE tenure_months < 0
    ) AS negative_tenure,

    COUNT(*) FILTER (
        WHERE monthly_charges < 0
    ) AS negative_monthly_charges,

    COUNT(*) FILTER (
        WHERE total_charges < 0
    ) AS negative_total_charges,

    COUNT(*) FILTER (
        WHERE churn_score < 0
        OR churn_score > 100
    ) AS invalid_churn_score,

    COUNT(*) FILTER (
        WHERE cltv < 0
    ) AS negative_cltv

FROM public.telco_customer_churn_clean;



-- =====================================================
-- 4. Validate churn labels and values
-- =====================================================

SELECT

    COUNT(*) FILTER (
        WHERE churn_label IS NULL
        OR churn_label NOT IN ('Yes', 'No')
    ) AS invalid_churn_labels,

    COUNT(*) FILTER (
        WHERE churn_value IS NULL
        OR churn_value NOT IN (0, 1)
    ) AS invalid_churn_values,

    COUNT(*) FILTER (

        WHERE

        (
            churn_label = 'Yes'
            AND churn_value <> 1
        )

        OR

        (
            churn_label = 'No'
            AND churn_value <> 0
        )

    ) AS label_value_mismatches

FROM public.telco_customer_churn_clean;



-- =====================================================
-- 5. Review missing churn reasons by churn status
-- =====================================================

SELECT

    churn_label,

    COUNT(*)
        AS total_customers,

    COUNT(churn_reason)
        AS customers_with_reason,

    COUNT(*) - COUNT(churn_reason)
        AS customers_without_reason

FROM public.telco_customer_churn_clean

GROUP BY churn_label

ORDER BY churn_label;