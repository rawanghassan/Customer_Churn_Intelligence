-- =====================================================
-- Project: Customer Churn Intelligence
-- File: 09_rule_based_risk_segmentation.sql
-- Purpose: Build a business rule-based churn risk segment
-- =====================================================


-- =====================================================
-- 1. Create customer risk segmentation view
-- =====================================================

DROP VIEW IF EXISTS public.customer_risk_segments;


CREATE VIEW public.customer_risk_segments AS

WITH scored_customers AS
(
    SELECT

        customer_id,

        tenure_months,

        contract,

        internet_service,

        tech_support,

        online_security,

        payment_method,

        paperless_billing,

        monthly_charges,

        churn_label,

        churn_value,


        -- Build an exploratory business risk score

        (

            CASE

                WHEN tenure_months <= 6
                    THEN 2

                WHEN tenure_months <= 12
                    THEN 1

                ELSE 0

            END


            +


            CASE

                WHEN contract = 'Month-to-month'
                    THEN 2

                ELSE 0

            END


            +


            CASE

                WHEN internet_service = 'Fiber optic'
                    THEN 1

                ELSE 0

            END


            +


            CASE

                WHEN tech_support = 'No'
                    THEN 1

                ELSE 0

            END


            +


            CASE

                WHEN online_security = 'No'
                    THEN 1

                ELSE 0

            END


            +


            CASE

                WHEN payment_method = 'Electronic check'
                    THEN 2

                ELSE 0

            END


            +


            CASE

                WHEN paperless_billing = 'Yes'
                    THEN 1

                ELSE 0

            END


            +


            CASE

                WHEN monthly_charges >= 75
                    THEN 1

                ELSE 0

            END

        ) AS risk_score


    FROM public.telco_customer_churn_clean
)


SELECT

    *,

    CASE

        WHEN risk_score >= 8
            THEN 'Very High Risk'

        WHEN risk_score >= 6
            THEN 'High Risk'

        WHEN risk_score >= 3
            THEN 'Moderate Risk'

        ELSE 'Low Risk'

    END AS risk_segment


FROM scored_customers;







SELECT

    risk_segment,

    COUNT(*) AS total_customers,

    SUM(churn_value) AS churned_customers,

    ROUND(
        AVG(churn_value) * 100,
        2
    ) AS churn_rate_percentage,

    ROUND(
        AVG(risk_score),
        2
    ) AS average_risk_score,

    ROUND(
        AVG(tenure_months),
        2
    ) AS average_tenure_months,

    ROUND(
        AVG(monthly_charges),
        2
    ) AS average_monthly_charges

FROM public.customer_risk_segments

GROUP BY risk_segment

ORDER BY

    CASE risk_segment

        WHEN 'Very High Risk'
            THEN 1

        WHEN 'High Risk'
            THEN 2

        WHEN 'Moderate Risk'
            THEN 3

        WHEN 'Low Risk'
            THEN 4

    END;