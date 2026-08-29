# Customer Churn Intelligence Case Study

## End-to-End SQL, Analytics, and Machine Learning Project

---

## 1. Project Overview

Customer Churn Intelligence is an end-to-end data analytics and machine-learning project developed to understand why telecommunications customers leave, identify the characteristics associated with churn risk, and generate practical business recommendations for retention.

The project integrates:

- SQL data validation and business analysis
- Exploratory data analysis in Python
- Data visualization
- Rule-based risk segmentation
- Logistic Regression modeling
- Customer-level churn scoring
- Business-oriented interpretation and recommendations

This case study presents the project as a complete business analytics solution rather than only a technical exercise.

---

## 2. Business Problem

Customer churn is one of the most important commercial challenges in subscription-based businesses. Losing existing customers affects:

- Revenue stability
- Customer lifetime value
- Acquisition efficiency
- Long-term business growth
- Competitive position

For a telecommunications company, churn does not only represent the loss of one customer. It can also signal deeper issues related to pricing, service quality, support experience, product fit, and competitive pressure.

The goal of this project was to answer the following key business questions:

1. What is the overall churn rate?
2. Which customer groups are most likely to churn?
3. Which services, contract types, and payment behaviors are associated with higher churn?
4. What are the most frequently reported reasons for churn?
5. Can churn risk be predicted using historical customer data?
6. How can the findings support practical customer-retention actions?

---

## 3. Project Objectives

The project was designed to achieve six main objectives:

- Validate and clean customer data using SQL.
- Explore churn patterns across contracts, tenure, services, and payment behaviors.
- Identify reported churn reasons and group them into business categories.
- Develop an initial rule-based customer risk segmentation framework.
- Build and evaluate a predictive churn model.
- Translate analytical findings into business recommendations.

---

## 4. Dataset Summary

The project used a telecommunications customer churn dataset containing:

- **7,043 customers**
- **33 variables**

The dataset included information related to:

- Customer demographics and household context
- Customer tenure
- Contract type
- Internet and phone services
- Technical support and online security
- Monthly charges and total charges
- Customer lifetime value (CLTV)
- Churn outcome
- Reported churn reasons

This dataset was sufficiently rich to support both descriptive analytics and predictive modeling.

---

## 5. Tools and Technologies

### Database and Querying
- PostgreSQL
- pgAdmin
- SQL

### Python Analytics Environment
- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-learn
- Logistic Regression

### Model and Artifact Saving
- Joblib
- JSON

---

## 6. Analytical Workflow

The project was completed in a structured sequence:

### Stage 1: Data Preparation in PostgreSQL
- Imported the raw customer dataset into PostgreSQL.
- Validated the structure and contents of the data.
- Checked duplicates, missing values, and label consistency.
- Created a clean analytical table.
- Audited data quality.

### Stage 2: Exploratory SQL Analysis
- Measured overall churn.
- Analyzed churn by contract type.
- Analyzed churn by customer tenure.
- Analyzed churn by internet service and support services.
- Analyzed churn by payment behavior and billing methods.
- Analyzed customer profile variables.
- Analyzed reported churn reasons.
- Built a rule-based risk segmentation view.

### Stage 3: Exploratory Data Analysis in Python
- Loaded the cleaned dataset into Python.
- Built visualizations for key churn patterns.
- Summarized the main analytical findings.
- Prepared the data for modeling.

### Stage 4: Predictive Modeling
- Prevented data leakage by excluding post-outcome variables.
- Split the data into training and testing subsets.
- Built a preprocessing and Logistic Regression pipeline.
- Evaluated model performance on an independent test set.
- Interpreted model coefficients.

### Stage 5: Output Generation
- Saved reusable models.
- Generated test-set predictions.
- Generated risk scores for all customers.
- Saved metadata and reproducibility artifacts.
- Documented the project in README and Case Study format.

---

## 7. Key Exploratory Findings

### 7.1 Overall Churn

The dataset contained:

- **7,043 total customers**
- **5,174 retained customers**
- **1,869 churned customers**

This corresponds to an overall churn rate of:

- **26.54%**

This means that approximately one out of every four customers left the company.

---

### 7.2 Contract Type

Contract type was one of the strongest differentiators of churn.

Observed churn rates:

- **Month-to-month:** 42.71%
- **One year:** 11.27%
- **Two year:** 2.83%

Approximately **88.6% of all churned customers** had month-to-month contracts.

This suggests that contract flexibility is strongly associated with customer exit risk.

---

### 7.3 Customer Tenure

Customer churn declined substantially as tenure increased.

Observed churn rates by tenure group:

- **0–6 months:** 52.94%
- **7–12 months:** 35.89%
- **13–24 months:** 28.71%
- **25–48 months:** 20.39%
- **49+ months:** 9.51%

The first six months represented the most vulnerable customer period.

This finding strongly suggests that early customer experience is critical for retention.

---

### 7.4 Internet Service and Service Experience

Observed churn rates by internet service:

- **Fiber optic:** 41.89%
- **DSL:** 18.96%
- **No internet service:** 7.40%

Observed churn rates by technical support:

- **No technical support:** 41.64%
- **With technical support:** 15.17%

Observed churn rates by online security:

- **No online security:** 41.77%
- **With online security:** 14.61%

These patterns suggest that product experience, support access, and service adoption are closely related to customer retention.

---

### 7.5 Billing and Payment Behavior

Payment behavior also showed clear churn differences.

Observed churn rates by payment method:

- **Electronic check:** 45.29%
- **Mailed check:** 19.11%
- **Bank transfer (automatic):** 16.71%
- **Credit card (automatic):** 15.24%

Observed churn rates by payment group:

- **Manual payment:** 34.67%
- **Automatic payment:** 15.98%

Observed churn rates by paperless billing:

- **Paperless billing = Yes:** 33.57%
- **Paperless billing = No:** 16.33%

These findings indicate that payment behavior may be a useful operational signal for retention programs.

---

### 7.6 Customer Profile

Additional customer-profile analysis showed that:

- Senior customers had higher churn than non-senior customers.
- Customers without partners or dependents had higher churn rates.
- Gender showed minimal difference and did not appear to be a major churn driver.

---

### 7.7 Reported Churn Reasons

Reported churn reasons were grouped into broader business categories.

Category shares among churned customers:

- **Competitor:** 33.23%
- **Service and Support:** 24.29%
- **Product and Network:** 18.08%
- **Price and Charges:** 13.00%
- **Other or Unknown:** 8.24%
- **Customer Circumstances:** 3.16%

Together, competitor, service, support, product, and network issues represented approximately **75.60%** of reported churn.

This indicates that churn is not driven by one single issue, but by a combination of service quality, market competition, and perceived value.

---

## 8. Rule-Based Customer Risk Segmentation

A rule-based risk segmentation framework was built as an exploratory business tool.

Customers were classified into:

- Low Risk
- Moderate Risk
- High Risk
- Very High Risk

Observed churn rates:

- **Low Risk:** 3.06%
- **Moderate Risk:** 15.59%
- **High Risk:** 35.02%
- **Very High Risk:** 62.75%

The High-Risk and Very-High-Risk groups represented approximately **42% of all customers**, but contained approximately **79.5% of all churned customers**.

This segmentation showed that relatively simple business rules can already isolate large portions of churn concentration.

However, the segmentation was not treated as a replacement for formally evaluated predictive modeling.

---

## 9. Machine-Learning Model

### 9.1 Model Selection

A **Logistic Regression** classifier was selected as the first predictive model because:

- It is interpretable.
- It performs well for binary classification.
- It supports business explanation.
- It is suitable for a strong baseline model.

### 9.2 Data-Leakage Prevention

To avoid data leakage, the following variables were excluded from model inputs:

- `customer_id`
- `churn_label`
- `churn_score`
- `churn_reason`

The target variable was:

- `churn_value`

### 9.3 Training Strategy

The model used:

- Stratified 80/20 train-test split
- Random state = 42
- Balanced class weights

### 9.4 Preprocessing

Numerical variables were processed with:

- Median imputation
- Standard scaling

Categorical variables were processed with:

- Most-frequent-value imputation
- One-hot encoding

These steps were integrated into a single machine-learning pipeline.

---

## 10. Model Performance

The Logistic Regression model was evaluated on an independent testing dataset.

### Performance Metrics

- **Accuracy:** 74.45%
- **Balanced Accuracy:** 76.03%
- **Precision:** 51.21%
- **Recall:** 79.41%
- **F1-Score:** 62.26%
- **ROC-AUC:** 85.70%

### Confusion Matrix Results

- **True Negatives:** 752
- **False Positives:** 283
- **False Negatives:** 77
- **True Positives:** 297

### Interpretation

The model correctly detected approximately **79% of customers who actually churned**.

This relatively high recall is useful in a retention setting, where failing to identify at-risk customers may be more costly than contacting some customers who ultimately remain.

The **ROC-AUC of 0.857** indicates strong discriminatory ability between customers with higher and lower churn risk.

Although the model produced some false positives, this tradeoff may be acceptable depending on retention costs and intervention strategy.

---

## 11. Key Model Associations

The final coefficient analysis identified several important associations.

### Higher Predicted Churn Was Associated With:
- Month-to-month contracts
- Fiber optic internet service
- Electronic-check payment
- Paperless billing
- Shorter customer tenure

### Lower Predicted Churn Was Associated With:
- Longer customer tenure
- Two-year contracts
- Having dependents
- DSL service
- No internet service

These coefficients describe conditional associations after accounting for the other variables in the model.

They should not be interpreted as evidence of direct causation.

Some variables such as monthly charges and total charges should be interpreted carefully, because they are strongly related to tenure, contracts, and service usage.

---

## 12. Business Recommendations

Based on the combined SQL, exploratory, and predictive findings, the following business recommendations were developed.

### 12.1 Prioritize the Early Customer Lifecycle
Retention efforts should be concentrated in the first six months through:
- Structured onboarding
- Welcome communications
- Early satisfaction checks
- Proactive support
- Service education

### 12.2 Develop Contract-Conversion Offers
Month-to-month customers should be evaluated for:
- One-year contract incentives
- Two-year contract incentives
- Loyalty rewards
- Bundle upgrades
- Retention-specific offers

### 12.3 Encourage Automatic Payment Adoption
Customers using electronic check and other manual payment methods may be targeted with:
- Automatic-payment discounts
- Simplified enrollment
- Loyalty incentives
- Payment reminders

### 12.4 Build a High-Risk Retention Workflow
A business workflow should combine:
- Predicted churn probability
- Customer lifetime value
- Contract information
- Service history
- Retention budget

### 12.5 Review the Fiber Optic Customer Experience
This segment should be investigated for:
- Price sensitivity
- Reliability issues
- Service-value perception
- Competitive pressure
- Complaint frequency

### 12.6 Strengthen Technical Support and Online Security Adoption
The company should test the impact of:
- Support bundles
- Security bundles
- Device-protection offers
- Service education

### 12.7 Improve Service and Support Quality
Because support-related reasons represented a large share of churn, the company should strengthen:
- Service staff training
- Complaint handling
- Resolution speed
- Customer follow-up
- Experience monitoring

### 12.8 Monitor Competitive Pressure
Because competitor-related reasons represented the largest category, the company should regularly monitor:
- Pricing
- Internet speed offers
- Data allowances
- Promotions
- Devices
- Contract terms

---

## 13. Business Value of the Project

This project provides practical business value in several ways:

- It identifies where churn is concentrated.
- It helps prioritize customers by predicted risk.
- It enables proactive rather than reactive retention.
- It supports operational targeting of high-risk customers.
- It links technical modeling to business recommendations.
- It creates reusable outputs for future scoring and monitoring.

The project does not only explain churn historically. It also provides a reusable framework for future retention decision-making.

---

## 14. Project Deliverables

The project produced the following artifacts:

### Analytical Files
- SQL scripts
- Python notebooks
- Exploratory charts
- Machine-learning notebook

### Saved Models
- `models/logistic_regression_evaluated.joblib`
- `models/logistic_regression_final.joblib`

### Output Files
- `outputs/test_set_churn_predictions.csv`
- `outputs/all_customer_churn_risk_scores.csv`
- `outputs/model_metadata.json`

### Reproducibility Files
- `requirements.txt`
- `environment_info.txt`

### Documentation
- `README.md`
- `Customer_Churn_Case_Study.md`

---

## 15. Limitations

The project should be interpreted with the following limitations in mind:

- The analysis identifies statistical associations rather than causal relationships.
- The model was evaluated using one stratified train-test split.
- External validation was not performed.
- The prediction threshold remained at 0.50.
- Probability calibration was not performed.
- Logistic Regression mainly captures linear relationships in the transformed feature space.
- The dataset may not represent every telecommunications market.

---

## 16. Future Improvements

Possible future extensions include:

- Cross-validation
- Threshold optimization
- Probability calibration
- Tree-based model comparison
- Cost-sensitive decision rules
- Customer lifetime value optimization
- Temporal validation
- Retention campaign testing
- Model monitoring over time

---

## 17. Final Conclusion

This project demonstrated how customer churn can be addressed through a combination of SQL analytics, exploratory analysis, data visualization, and predictive modeling.

The findings showed that churn is especially concentrated among:

- Short-tenure customers
- Month-to-month customers
- Fiber optic customers
- Customers without support and security services
- Customers using electronic check and manual payment behavior

The Logistic Regression model delivered strong recall and good overall discriminatory performance, making it useful as a first-stage churn-risk identification tool.

Most importantly, the project translated technical findings into clear business recommendations.

As a result, Customer Churn Intelligence serves as both:

1. A complete analytics and machine-learning portfolio project
2. A practical retention-analysis framework that could support real business decision-making