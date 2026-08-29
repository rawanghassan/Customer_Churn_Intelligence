-- =====================================================
-- Project: Customer Churn Intelligence
-- File: 05_contract_and_tenure_analysis.sql
-- Purpose: Analyze churn by contract type and tenure
-- =====================================================


-- =====================================================
-- 1. Churn performance by contract type
-- =====================================================

SELECT

    contract,

    COUNT(*) AS total_customers,

    SUM(churn_value) AS churned_customers,

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
    ) AS average_monthly_charges

FROM public.telco_customer_churn_clean

GROUP BY contract

ORDER BY churn_rate_percentage DESC;



-- =====================================================
-- 2. Churn performance by customer tenure group
-- =====================================================

WITH tenure_groups AS
(
    SELECT

        CASE

            WHEN tenure_months <= 6
                THEN '0-6 Months'

            WHEN tenure_months <= 12
                THEN '7-12 Months'

            WHEN tenure_months <= 24
                THEN '13-24 Months'

            WHEN tenure_months <= 48
                THEN '25-48 Months'

            ELSE '49+ Months'

        END AS tenure_group,

        CASE

            WHEN tenure_months <= 6
                THEN 1

            WHEN tenure_months <= 12
                THEN 2

            WHEN tenure_months <= 24
                THEN 3

            WHEN tenure_months <= 48
                THEN 4

            ELSE 5

        END AS group_order,

        churn_value,

        monthly_charges

    FROM public.telco_customer_churn_clean
)

SELECT

    tenure_group,

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

FROM tenure_groups

GROUP BY
    tenure_group,
    group_order

ORDER BY group_order;