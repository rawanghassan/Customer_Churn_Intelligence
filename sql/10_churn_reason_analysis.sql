-- =====================================================
-- Project: Customer Churn Intelligence
-- File: 10_churn_reason_analysis.sql
-- Purpose: Analyze the reported reasons for churn
-- =====================================================


-- =====================================================
-- 1. Top individual churn reasons
-- =====================================================

SELECT

    churn_reason,

    COUNT(*) AS churned_customers,

    ROUND(

        COUNT(*) * 100.0
        / SUM(COUNT(*)) OVER (),

        2

    ) AS share_of_churned_customers

FROM public.telco_customer_churn_clean

WHERE churn_value = 1

GROUP BY churn_reason

ORDER BY churned_customers DESC;



-- =====================================================
-- 2. Group churn reasons into business categories
-- =====================================================

WITH categorized_reasons AS
(
    SELECT

        customer_id,

        churn_reason,

        CASE

            WHEN churn_reason ILIKE '%competitor%'
                THEN 'Competitor'

            WHEN churn_reason ILIKE '%price%'
                OR churn_reason ILIKE '%charge%'
                OR churn_reason ILIKE '%affordable%'
                THEN 'Price and Charges'

            WHEN churn_reason ILIKE '%support%'
                OR churn_reason ILIKE '%attitude%'
                OR churn_reason ILIKE '%self-service%'
                OR churn_reason ILIKE '%service provider%'
                THEN 'Service and Support'

            WHEN churn_reason ILIKE '%network%'
                OR churn_reason ILIKE '%reliability%'
                OR churn_reason ILIKE '%product%'
                OR churn_reason ILIKE '%service%'
                OR churn_reason ILIKE '%download%'
                OR churn_reason ILIKE '%upload%'
                OR churn_reason ILIKE '%device%'
                OR churn_reason ILIKE '%data%'
                THEN 'Product and Network'

            WHEN churn_reason ILIKE '%moved%'
                OR churn_reason ILIKE '%deceased%'
                THEN 'Customer Circumstances'

            ELSE 'Other or Unknown'

        END AS churn_reason_category

    FROM public.telco_customer_churn_clean

    WHERE churn_value = 1
)

SELECT

    churn_reason_category,

    COUNT(*) AS churned_customers,

    ROUND(

        COUNT(*) * 100.0
        / SUM(COUNT(*)) OVER (),

        2

    ) AS share_of_churned_customers

FROM categorized_reasons

GROUP BY churn_reason_category

ORDER BY churned_customers DESC;