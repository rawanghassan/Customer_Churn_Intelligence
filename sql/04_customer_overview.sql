-- =====================================================
-- Project: Customer Churn Intelligence
-- File: 04_customer_overview.sql
-- Purpose: Build an executive overview of customer churn
-- =====================================================


-- =====================================================
-- 1. Overall customer KPIs
-- =====================================================

SELECT

    COUNT(*) AS total_customers,

    SUM(churn_value) AS churned_customers,

    COUNT(*) - SUM(churn_value)
        AS retained_customers,

    ROUND(
        AVG(churn_value) * 100,
        2
    ) AS churn_rate_percentage,

    ROUND(
        AVG(tenure_months),
        2
    ) AS average_tenure_months,

    ROUND(
        AVG(monthly_charges),
        2
    ) AS average_monthly_charges,

    ROUND(
        AVG(total_charges),
        2
    ) AS average_total_charges,

    ROUND(
        AVG(cltv),
        2
    ) AS average_customer_lifetime_value

FROM public.telco_customer_churn_clean;



-- =====================================================
-- 2. Compare retained and churned customers
-- =====================================================

SELECT

    churn_label,

    COUNT(*) AS total_customers,

    ROUND(
        COUNT(*) * 100.0
        / SUM(COUNT(*)) OVER (),
        2
    ) AS customer_share_percentage,

    ROUND(
        AVG(tenure_months),
        2
    ) AS average_tenure_months,

    ROUND(
        AVG(monthly_charges),
        2
    ) AS average_monthly_charges,

    ROUND(
        AVG(total_charges),
        2
    ) AS average_total_charges,

    ROUND(
        AVG(churn_score),
        2
    ) AS average_churn_score,

    ROUND(
        AVG(cltv),
        2
    ) AS average_cltv

FROM public.telco_customer_churn_clean

GROUP BY churn_label

ORDER BY churn_label;