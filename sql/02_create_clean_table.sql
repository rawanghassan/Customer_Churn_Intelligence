-- =====================================================
-- Project: Customer Churn Intelligence
-- File: 02_create_clean_table.sql
-- Purpose: Create a clean analytical customer table
-- =====================================================


-- Remove the clean table if it already exists

DROP TABLE IF EXISTS public.telco_customer_churn_clean;


-- Create the clean customer table

CREATE TABLE public.telco_customer_churn_clean AS

SELECT

    -- Customer identification

    TRIM(customer_id) AS customer_id,

    NULLIF(TRIM(customer_count), '')::INTEGER
        AS customer_count,


    -- Geographic information

    NULLIF(TRIM(country), '')
        AS country,

    NULLIF(TRIM(state), '')
        AS state,

    NULLIF(TRIM(city), '')
        AS city,

    NULLIF(TRIM(zip_code), '')
        AS zip_code,

    NULLIF(TRIM(lat_long), '')
        AS lat_long,

    NULLIF(TRIM(latitude), '')::NUMERIC(10,6)
        AS latitude,

    NULLIF(TRIM(longitude), '')::NUMERIC(10,6)
        AS longitude,


    -- Customer characteristics

    NULLIF(TRIM(gender), '')
        AS gender,

    NULLIF(TRIM(senior_citizen), '')
        AS senior_citizen,

    NULLIF(TRIM(partner), '')
        AS partner,

    NULLIF(TRIM(dependents), '')
        AS dependents,


    -- Customer relationship

    NULLIF(TRIM(tenure_months), '')::INTEGER
        AS tenure_months,


    -- Services

    NULLIF(TRIM(phone_service), '')
        AS phone_service,

    NULLIF(TRIM(multiple_lines), '')
        AS multiple_lines,

    NULLIF(TRIM(internet_service), '')
        AS internet_service,

    NULLIF(TRIM(online_security), '')
        AS online_security,

    NULLIF(TRIM(online_backup), '')
        AS online_backup,

    NULLIF(TRIM(device_protection), '')
        AS device_protection,

    NULLIF(TRIM(tech_support), '')
        AS tech_support,

    NULLIF(TRIM(streaming_tv), '')
        AS streaming_tv,

    NULLIF(TRIM(streaming_movies), '')
        AS streaming_movies,


    -- Contract and payment information

    NULLIF(TRIM(contract), '')
        AS contract,

    NULLIF(TRIM(paperless_billing), '')
        AS paperless_billing,

    NULLIF(TRIM(payment_method), '')
        AS payment_method,


    -- Financial information

    NULLIF(TRIM(monthly_charges), '')::NUMERIC(10,2)
        AS monthly_charges,

    NULLIF(TRIM(total_charges), '')::NUMERIC(12,2)
        AS total_charges,


    -- Churn information

    NULLIF(TRIM(churn_label), '')
        AS churn_label,

    NULLIF(TRIM(churn_value), '')::INTEGER
        AS churn_value,

    NULLIF(TRIM(churn_score), '')::INTEGER
        AS churn_score,

    NULLIF(TRIM(cltv), '')::INTEGER
        AS cltv,

    NULLIF(TRIM(churn_reason), '')
        AS churn_reason

FROM public.telco_customer_churn_raw;



ALTER TABLE public.telco_customer_churn_clean

ADD CONSTRAINT
telco_customer_churn_clean_pk

PRIMARY KEY (customer_id);


SELECT COUNT(*) AS total_clean_customers

FROM public.telco_customer_churn_clean;