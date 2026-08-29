# Customer Churn Intelligence

## SQL Analytics, Customer Segmentation, and Machine Learning

Customer Churn Intelligence is an end-to-end data analytics and machine-learning project designed to identify customer churn patterns, evaluate customer-risk factors, and generate actionable retention recommendations.

The project combines:

- PostgreSQL
- SQL
- Python
- Exploratory Data Analysis
- Customer Risk Segmentation
- Logistic Regression
- Model Evaluation
- Business Recommendations

---

## Business Problem

Customer churn directly affects revenue, customer lifetime value, and long-term business growth.

The main objectives of this project are to:

- Measure the overall customer churn rate.
- Identify customer groups with elevated churn risk.
- Analyze churn across contracts, services, tenure, and payment methods.
- Investigate the most frequently reported churn reasons.
- Build a predictive model for customer churn.
- Generate customer-level churn probabilities.
- Translate analytical findings into practical retention recommendations.

---

## Dataset

The project uses a telecommunications customer churn dataset containing:

- **7,043 customers**
- **33 original variables**

The dataset includes information related to:

- Customer characteristics
- Customer tenure
- Internet and phone services
- Technical support
- Online security
- Contract type
- Payment behavior
- Monthly charges
- Total charges
- Customer lifetime value
- Churn status
- Reported churn reasons

---

## Project Workflow

1. Raw data validation
2. PostgreSQL database creation
3. Data import into PostgreSQL
4. SQL data cleaning
5. Data-quality auditing
6. Exploratory SQL analysis
7. Rule-based customer-risk segmentation
8. Python exploratory data analysis
9. Data visualization
10. Machine-learning preprocessing
11. Logistic Regression model training
12. Independent model evaluation
13. Model interpretation
14. Customer churn-risk scoring
15. Business recommendation development
16. Reproducibility and project documentation

---

## Technology Stack

### Database

- PostgreSQL
- pgAdmin

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn
- Logistic Regression

### Model Persistence

- Joblib

### Development Environment

- Jupyter Notebook
- Python Virtual Environment

---

## SQL Analysis

The SQL workflow included:

- Raw data validation
- Duplicate-customer checks
- Missing-value analysis
- Data-type conversion
- Numerical-range validation
- Churn-label validation
- Customer overview analysis
- Contract analysis
- Tenure analysis
- Service-risk analysis
- Billing and payment analysis
- Customer-profile analysis
- Rule-based customer-risk segmentation
- Churn-reason analysis

---

## Key Exploratory Findings

### Overall Churn

- Total customers: **7,043**
- Retained customers: **5,174**
- Churned customers: **1,869**
- Overall churn rate: **26.54%**

Approximately one out of every four customers left the company.

### Contract Type

- Month-to-month: **42.71%**
- One year: **11.27%**
- Two year: **2.83%**

Approximately **88.6% of all churned customers** had month-to-month contracts.

### Customer Tenure

- 0–6 months: **52.94%**
- 7–12 months: **35.89%**
- 13–24 months: **28.71%**
- 25–48 months: **20.39%**
- 49+ months: **9.51%**

The first six months represent the highest observed customer-risk period.

### Internet Service

- Fiber optic: **41.89%**
- DSL: **18.96%**
- No internet service: **7.40%**

### Technical Support

- No technical support: **41.64%**
- Technical support enabled: **15.17%**

### Online Security

- No online security: **41.77%**
- Online security enabled: **14.61%**

### Payment Behavior

- Electronic check: **45.29%**
- Mailed check: **19.11%**
- Automatic bank transfer: **16.71%**
- Automatic credit card: **15.24%**

Manual-payment customers recorded a churn rate of **34.67%**, compared with **15.98%** among automatic-payment customers.

### Reported Churn Reasons

- Competitor: **33.23%**
- Service and support: **24.29%**
- Product and network: **18.08%**
- Price and charges: **13.00%**
- Other or unknown: **8.24%**
- Customer circumstances: **3.16%**

Competitor, service, support, product, and network categories together represented approximately **75.60%** of reported churn.

---

## Rule-Based Customer Risk Segmentation

Observed churn rates:

- Low Risk: **3.06%**
- Moderate Risk: **15.59%**
- High Risk: **35.02%**
- Very High Risk: **62.75%**

The High-Risk and Very-High-Risk groups represented approximately **42% of customers** but contained approximately **79.5% of all churned customers**.

This segmentation is exploratory and is not presented as a substitute for independently evaluated predictive modeling.

---

## Machine-Learning Model

### Model

Logistic Regression

### Training Strategy

- 80% training data
- 20% testing data
- Stratified train-test split
- Random state: 42
- Balanced class weights

### Preprocessing

Numerical variables:

- Median imputation
- Standard scaling

Categorical variables:

- Most-frequent-value imputation
- One-hot encoding

---

## Data-Leakage Prevention

The following variables were excluded from predictive inputs:

- `customer_id`
- `churn_label`
- `churn_score`
- `churn_reason`

The target variable was:

`churn_value`

The preprocessing pipeline was fitted using training data only.

---

## Model Performance

| Metric | Score |
|---|---:|
| Accuracy | 74.45% |
| Balanced Accuracy | 76.03% |
| Precision | 51.21% |
| Recall | 79.41% |
| F1-Score | 62.26% |
| ROC-AUC | 85.70% |

The model correctly identified approximately **79% of customers who actually churned**.

The ROC-AUC score of **0.857** indicates strong ability to distinguish between customers with higher and lower churn risk.

---

## Confusion Matrix

- True Negatives: **752**
- False Positives: **283**
- False Negatives: **77**
- True Positives: **297**

The final operating threshold should depend on retention-intervention cost, customer value, available business resources, and acceptable false-positive volume.

---

## Key Model Associations

Factors associated with higher predicted churn included:

- Month-to-month contracts
- Fiber optic internet service
- Electronic-check payment
- Paperless billing
- Shorter customer tenure

Factors associated with lower predicted churn included:

- Longer customer tenure
- Two-year contracts
- Having dependents
- DSL service
- No internet service

Model coefficients represent conditional statistical associations and should not be interpreted as direct causal effects.

---

## Business Recommendations

### 1. Prioritize Early Customer Retention

Focus retention efforts during the first six months through structured onboarding, welcome communications, satisfaction checks, proactive technical support, and service education.

### 2. Develop Contract-Conversion Programs

Encourage suitable month-to-month customers to move toward longer contracts using loyalty rewards, annual-contract incentives, service upgrades, and bundled benefits.

### 3. Encourage Automatic Payment

Test simplified automatic-payment enrollment, small discounts, loyalty benefits, and payment reminders.

### 4. Build a High-Risk Retention Workflow

Prioritize customers using predicted churn probability, customer lifetime value, contract type, service history, and available retention resources.

### 5. Review Fiber Optic Customer Experience

Investigate service reliability, pricing, network quality, customer expectations, complaint frequency, and competitor offerings.

### 6. Strengthen Technical Support and Security Services

Evaluate bundled packages containing technical support, online security, device protection, and customer education.

### 7. Improve Customer-Service Quality

Strengthen staff training, response-time monitoring, complaint resolution, and customer-feedback processes.

### 8. Monitor Competitive Pressure

Regularly benchmark competitor pricing, download speeds, data allowances, device offers, promotions, and contract conditions.

---

## Project Outputs

### Customer Predictions

`outputs/test_set_churn_predictions.csv`

Contains:

- Actual churn outcome
- Predicted churn outcome
- Churn probability
- Customer risk segment

### All-Customer Risk Scores

`outputs/all_customer_churn_risk_scores.csv`

Contains churn probabilities and risk segments for all customers.

### Model Metadata

`outputs/model_metadata.json`

Contains model configuration, evaluation metrics, feature information, confusion-matrix results, and model notes.

---

## Saved Models

`models/logistic_regression_evaluated.joblib`

The evaluated model trained using the training subset.

`models/logistic_regression_final.joblib`

The final model retrained using all available labeled customer data.

---

## Project Structure

```text
Customer_Churn_Intelligence
│
├── data
├── sql
├── notebooks
├── images
├── models
├── outputs
├── documentation
├── requirements.txt
├── environment_info.txt
└── README.md
```

---

## How to Run the Project

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Start Jupyter Notebook:

```bash
python -m notebook
```

Open:

- `notebooks/01_customer_churn_eda.ipynb`
- `notebooks/02_customer_churn_model.ipynb`

Then use **Kernel → Restart and Run All**.

---

## Limitations

- The analysis identifies statistical associations rather than causal relationships.
- The model was evaluated using one stratified train-test split.
- External validation was not performed.
- The default prediction threshold of 0.50 was retained.
- Probability calibration was not performed.
- Logistic Regression primarily captures linear relationships in the transformed feature space.
- The dataset may not represent every telecommunications market or current customer environment.

---

## Future Improvements

- Cross-validation
- Threshold optimization
- Probability calibration
- Tree-based model comparison
- Cost-sensitive modeling
- Customer-lifetime-value optimization
- Temporal validation
- Model monitoring
- External validation
- Retention-experiment evaluation

---

## Project Status

**Completed**

The project includes SQL analysis, data cleaning, data-quality validation, customer segmentation, Python exploratory analysis, data visualizations, Logistic Regression modeling, independent model evaluation, customer churn-risk scoring, reusable model artifacts, reproducibility files, and business recommendations.
