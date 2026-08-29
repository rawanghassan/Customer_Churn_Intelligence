-- =====================================================
-- Project: Customer Churn Intelligence
-- File: 07_billing_and_payment_analysis.sql
-- Purpose: Analyze churn by billing and payment method
-- =====================================================


-- =====================================================
-- 1. Churn by payment method
-- =====================================================

SELECT

    payment_method,

    COUNT(*) AS total_customers,

    SUM(churn_value) AS churned_customers,

    ROUND(
        AVG(churn_value) * 100,
        2
    ) AS churn_rate_percentage,

    ROUND(
        AVG(monthly_charges),
        2
    ) AS average_monthly_charges

FROM public.telco_customer_churn_clean

GROUP BY payment_method

ORDER BY churn_rate_percentage DESC;



-- =====================================================
-- 2. Churn by paperless billing status
-- =====================================================

SELECT

    paperless_billing,

    COUNT(*) AS total_customers,

    SUM(churn_value) AS churned_customers,

    ROUND(
        AVG(churn_value) * 100,
        2
    ) AS churn_rate_percentage,

    ROUND(
        AVG(monthly_charges),
        2
    ) AS average_monthly_charges

FROM public.telco_customer_churn_clean

GROUP BY paperless_billing

ORDER BY churn_rate_percentage DESC;



-- =====================================================
-- 3. Compare automatic and manual payment groups
-- =====================================================

WITH payment_groups AS
(
    SELECT

        CASE

            WHEN payment_method IN
            (
                'Bank transfer (automatic)',
                'Credit card (automatic)'
            )
            THEN 'Automatic Payment'

            ELSE 'Manual Payment'

        END AS payment_group,

        churn_value,

        monthly_charges,

        tenure_months

    FROM public.telco_customer_churn_clean
)

SELECT

    payment_group,

    COUNT(*) AS total_customers,

    SUM(churn_value) AS churned_customers,

    ROUND(
        AVG(churn_value) * 100,
        2
    ) AS churn_rate_percentage,

    ROUND(
        AVG(monthly_charges),
        2
    ) AS average_monthly_charges,

    ROUND(
        AVG(tenure_months),
        2
    ) AS average_tenure_months

FROM payment_groups

GROUP BY payment_group

ORDER BY churn_rate_percentage DESC;