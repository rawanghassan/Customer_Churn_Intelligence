-- =====================================================
-- Project: Customer Churn Intelligence
-- File: 06_service_risk_analysis.sql
-- Purpose: Analyze churn by internet and support services
-- =====================================================


-- =====================================================
-- 1. Churn by internet service type
-- =====================================================

SELECT

    internet_service,

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

GROUP BY internet_service

ORDER BY churn_rate_percentage DESC;



-- =====================================================
-- 2. Churn by technical support status
-- =====================================================

SELECT

    tech_support,

    COUNT(*) AS total_customers,

    SUM(churn_value) AS churned_customers,

    ROUND(
        AVG(churn_value) * 100,
        2
    ) AS churn_rate_percentage

FROM public.telco_customer_churn_clean

GROUP BY tech_support

ORDER BY churn_rate_percentage DESC;



-- =====================================================
-- 3. Churn by online security status
-- =====================================================

SELECT

    online_security,

    COUNT(*) AS total_customers,

    SUM(churn_value) AS churned_customers,

    ROUND(
        AVG(churn_value) * 100,
        2
    ) AS churn_rate_percentage

FROM public.telco_customer_churn_clean

GROUP BY online_security

ORDER BY churn_rate_percentage DESC;