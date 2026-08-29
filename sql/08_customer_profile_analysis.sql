-- =====================================================
-- Project: Customer Churn Intelligence
-- File: 08_customer_profile_analysis.sql
-- Purpose: Analyze churn by customer characteristics
-- =====================================================


-- =====================================================
-- 1. Churn by senior citizen status
-- =====================================================

SELECT

    senior_citizen,

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

GROUP BY senior_citizen

ORDER BY churn_rate_percentage DESC;



-- =====================================================
-- 2. Churn by partner status
-- =====================================================

SELECT

    partner,

    COUNT(*) AS total_customers,

    SUM(churn_value) AS churned_customers,

    ROUND(
        AVG(churn_value) * 100,
        2
    ) AS churn_rate_percentage,

    ROUND(
        AVG(tenure_months),
        2
    ) AS average_tenure_months

FROM public.telco_customer_churn_clean

GROUP BY partner

ORDER BY churn_rate_percentage DESC;



-- =====================================================
-- 3. Churn by dependent status
-- =====================================================

SELECT

    dependents,

    COUNT(*) AS total_customers,

    SUM(churn_value) AS churned_customers,

    ROUND(
        AVG(churn_value) * 100,
        2
    ) AS churn_rate_percentage,

    ROUND(
        AVG(tenure_months),
        2
    ) AS average_tenure_months

FROM public.telco_customer_churn_clean

GROUP BY dependents

ORDER BY churn_rate_percentage DESC;



-- =====================================================
-- 4. Churn by gender
-- =====================================================

SELECT

    gender,

    COUNT(*) AS total_customers,

    SUM(churn_value) AS churned_customers,

    ROUND(
        AVG(churn_value) * 100,
        2
    ) AS churn_rate_percentage

FROM public.telco_customer_churn_clean

GROUP BY gender

ORDER BY churn_rate_percentage DESC;