#!/usr/bin/env python
# coding: utf-8

# # Customer Churn Prediction Model
# 
# ## Logistic Regression Classification
# 
# This notebook prepares customer data, builds a machine-learning pipeline, trains a Logistic Regression model, evaluates predictive performance, and interprets the main factors associated with customer churn.

# In[1]:


# Import required libraries

from pathlib import Path

import numpy as np
import pandas as pd


# Improve table display

pd.set_option(
    "display.max_columns",
    None
)


# Define the exact dataset path

data_path = Path(
    r"C:\Users\hp15-da\Desktop\معرض عمال\Customer_Churn_Intelligence\data\telco_customer_churn_clean.csv"
)


# Load the cleaned dataset

df = pd.read_csv(
    data_path
)


print(
    "Dataset loaded successfully."
)

print(
    f"Dataset shape: {df.shape}"
)


# In[2]:


# Preserve customer IDs for future prediction outputs

customer_ids = (

    df["customer_id"]

    .copy()

)


# Define columns excluded from model training

columns_to_exclude = [

    # Customer identifier

    "customer_id",


    # Constant or non-predictive fields

    "customer_count",

    "country",

    "state",


    # High-cardinality geographic fields

    "city",

    "zip_code",

    "lat_long",

    "latitude",

    "longitude",


    # Target or data-leakage fields

    "churn_label",

    "churn_value",

    "churn_score",

    "churn_reason"

]


# Create model features

X = (

    df

    .drop(

        columns=columns_to_exclude

    )

    .copy()

)


# Create the target variable

y = (

    df["churn_value"]

    .astype(int)

    .copy()

)


print(

    f"Feature matrix shape: {X.shape}"

)

print(

    f"Target vector shape: {y.shape}"

)


# In[3]:


# Review the target-class distribution

target_distribution = (

    y

    .value_counts()

    .sort_index()

    .rename_axis(
        "churn_value"
    )

    .reset_index(
        name="customer_count"
    )

)


target_distribution[
    "percentage"
] = (

    target_distribution[
        "customer_count"
    ]

    / len(y)

    * 100

)


target_distribution[
    "percentage"
] = (

    target_distribution[
        "percentage"
    ]

    .round(2)

)


target_distribution


# ## 1. Train–Test Split and Data Preprocessing
# 
# The dataset is divided into training and testing subsets using stratified sampling to preserve the original churn distribution.
# 
# Numerical features are standardized, while categorical features are converted into machine-readable variables using one-hot encoding.

# In[4]:


# Import preprocessing and model-selection tools

from sklearn.compose import ColumnTransformer

from sklearn.impute import SimpleImputer

from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)


print(
    "Preprocessing tools imported successfully."
)


# In[5]:


# Define numerical model features

numerical_features = [

    "tenure_months",

    "monthly_charges",

    "total_charges",

    "cltv"

]


# Identify the remaining categorical features

categorical_features = [

    column

    for column in X.columns

    if column not in numerical_features

]


print(
    f"Number of numerical features: "
    f"{len(numerical_features)}"
)


print(
    f"Number of categorical features: "
    f"{len(categorical_features)}"
)


print(
    "\nNumerical features:"
)


print(
    numerical_features
)


print(
    "\nCategorical features:"
)


print(
    categorical_features
)


# In[6]:


# Split the dataset into training and testing subsets

X_train, X_test, y_train, y_test = (

    train_test_split(

        X,

        y,

        test_size=0.20,

        random_state=42,

        stratify=y

    )

)


print(
    f"X_train shape: {X_train.shape}"
)


print(
    f"X_test shape: {X_test.shape}"
)


print(
    f"y_train shape: {y_train.shape}"
)


print(
    f"y_test shape: {y_test.shape}"
)


# In[7]:


# Confirm churn distribution across train and test sets

split_distribution = pd.DataFrame(

    {

        "Full Dataset": (

            y.value_counts(

                normalize=True

            )

            .sort_index()

            * 100

        ),


        "Training Set": (

            y_train.value_counts(

                normalize=True

            )

            .sort_index()

            * 100

        ),


        "Testing Set": (

            y_test.value_counts(

                normalize=True

            )

            .sort_index()

            * 100

        )

    }

)


split_distribution.index = [

    "Retained (0)",

    "Churned (1)"

]


split_distribution = (

    split_distribution

    .round(2)

)


split_distribution


# In[8]:


# Build the numerical preprocessing pipeline

numerical_transformer = Pipeline(

    steps=[

        (

            "imputer",

            SimpleImputer(

                strategy="median"

            )

        ),

        (

            "scaler",

            StandardScaler()

        )

    ]

)


# Build the categorical preprocessing pipeline

categorical_transformer = Pipeline(

    steps=[

        (

            "imputer",

            SimpleImputer(

                strategy="most_frequent"

            )

        ),

        (

            "onehot",

            OneHotEncoder(

                handle_unknown="ignore",

                drop="if_binary"

            )

        )

    ]

)


# Combine numerical and categorical preprocessing

preprocessor = ColumnTransformer(

    transformers=[

        (

            "numerical",

            numerical_transformer,

            numerical_features

        ),

        (

            "categorical",

            categorical_transformer,

            categorical_features

        )

    ]

)


print(
    "Preprocessing pipeline created successfully."
)


# ## 2. Logistic Regression Model Training
# 
# A Logistic Regression classifier is trained using a unified machine-learning pipeline that combines preprocessing and classification.
# 
# Class weighting is applied to reduce the effect of class imbalance and improve the model's ability to identify customers at risk of churn.

# In[9]:


# Import the Logistic Regression classifier

from sklearn.linear_model import LogisticRegression


print(
    "Logistic Regression imported successfully."
)


# In[10]:


# Build the complete machine-learning pipeline

logistic_model = Pipeline(

    steps=[

        (

            "preprocessor",

            preprocessor

        ),

        (

            "classifier",

            LogisticRegression(

                solver="liblinear",

                max_iter=1000,

                class_weight="balanced",

                random_state=42

            )

        )

    ]

)


print(
    "Logistic Regression pipeline created successfully."
)


# In[11]:


class_weight="balanced"


# In[12]:


# Train the Logistic Regression model

logistic_model.fit(

    X_train,

    y_train

)


print(
    "Logistic Regression model trained successfully."
)


# In[13]:


# Generate class predictions for the testing data

y_pred = (

    logistic_model

    .predict(

        X_test

    )

)


# Generate churn probabilities

y_pred_probability = (

    logistic_model

    .predict_proba(

        X_test

    )

    [:, 1]

)


print(
    "Testing predictions generated successfully."
)


print(

    f"Number of predictions: "

    f"{len(y_pred):,}"

)


print(

    f"Number of churn probabilities: "

    f"{len(y_pred_probability):,}"

)


# In[14]:


# Preview the first 10 model predictions

prediction_preview = pd.DataFrame(

    {

        "Actual Churn": (

            y_test

            .reset_index(

                drop=True

            )

        ),

        "Predicted Churn": (

            y_pred

        ),

        "Churn Probability": (

            y_pred_probability

        )

    }

)


prediction_preview[

    "Churn Probability"

] = (

    prediction_preview[

        "Churn Probability"

    ]

    .round(4)

)


prediction_preview.head(10)


# ## 3. Model Performance Evaluation
# 
# The trained Logistic Regression model is evaluated using multiple classification metrics.
# 
# Because customer churn is an imbalanced classification problem, model performance is assessed using precision, recall, F1-score, balanced accuracy, ROC-AUC, and the confusion matrix rather than relying on accuracy alone.

# In[15]:


# Import model-evaluation tools

import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve
)


print(
    "Model-evaluation tools imported successfully."
)


# In[16]:


# Calculate classification-performance metrics

accuracy = accuracy_score(
    y_test,
    y_pred
)


balanced_accuracy = balanced_accuracy_score(
    y_test,
    y_pred
)


precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)


recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)


f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)


roc_auc = roc_auc_score(
    y_test,
    y_pred_probability
)


# Create a model-performance summary

model_metrics = pd.DataFrame(
    {
        "Metric": [
            "Accuracy",
            "Balanced Accuracy",
            "Precision",
            "Recall",
            "F1-Score",
            "ROC-AUC"
        ],

        "Score": [
            accuracy,
            balanced_accuracy,
            precision,
            recall,
            f1,
            roc_auc
        ]
    }
)


model_metrics[
    "Score"
] = (

    model_metrics[
        "Score"
    ]

    .round(4)

)


model_metrics


# In[17]:


# Display the complete classification report

classification_results = classification_report(

    y_test,

    y_pred,

    target_names=[

        "Retained",

        "Churned"

    ],

    zero_division=0

)


print(
    classification_results
)


# In[18]:


# Calculate the confusion matrix

confusion_matrix_values = confusion_matrix(

    y_test,

    y_pred

)


# Extract individual classification outcomes

true_negatives, false_positives, false_negatives, true_positives = (

    confusion_matrix_values.ravel()

)


confusion_summary = pd.DataFrame(

    {

        "Outcome": [

            "True Negatives",

            "False Positives",

            "False Negatives",

            "True Positives"

        ],

        "Customers": [

            true_negatives,

            false_positives,

            false_negatives,

            true_positives

        ]

    }

)


confusion_summary


# In[19]:


# Define the project images folder

project_path = Path(

    r"C:\Users\hp15-da\Desktop\معرض عمال\Customer_Churn_Intelligence"

)


images_path = (

    project_path

    / "images"

)


images_path.mkdir(

    parents=True,

    exist_ok=True

)


# Create the confusion-matrix visualization

fig, ax = plt.subplots(

    figsize=(8, 6)

)


display = ConfusionMatrixDisplay(

    confusion_matrix=(

        confusion_matrix_values

    ),

    display_labels=[

        "Retained",

        "Churned"

    ]

)


display.plot(

    ax=ax,

    values_format="d"

)


ax.set_title(

    "Logistic Regression Confusion Matrix",

    fontsize=15,

    fontweight="bold",

    pad=16

)


plt.tight_layout()


# Save the chart

confusion_matrix_path = (

    images_path

    / "12_confusion_matrix.png"

)


plt.savefig(

    confusion_matrix_path,

    dpi=300,

    bbox_inches="tight"

)


plt.show()


print(

    f"Chart saved successfully:\n"

    f"{confusion_matrix_path}"

)


# In[20]:


# Calculate the ROC curve

false_positive_rate, true_positive_rate, thresholds = (

    roc_curve(

        y_test,

        y_pred_probability

    )

)


# Create the ROC-curve visualization

fig, ax = plt.subplots(

    figsize=(8, 6)

)


ax.plot(

    false_positive_rate,

    true_positive_rate,

    linewidth=2,

    label=(

        f"Logistic Regression "

        f"(AUC = {roc_auc:.3f})"

    )

)


ax.plot(

    [0, 1],

    [0, 1],

    linestyle="--",

    label="Random Classifier"

)


ax.set_title(

    "Receiver Operating Characteristic Curve",

    fontsize=15,

    fontweight="bold",

    pad=16

)


ax.set_xlabel(

    "False Positive Rate",

    fontsize=12

)


ax.set_ylabel(

    "True Positive Rate",

    fontsize=12

)


ax.legend(

    loc="lower right"

)


plt.tight_layout()


# Save the chart

roc_curve_path = (

    images_path

    / "13_roc_curve.png"

)


plt.savefig(

    roc_curve_path,

    dpi=300,

    bbox_inches="tight"

)


plt.show()


print(

    f"Chart saved successfully:\n"

    f"{roc_curve_path}"

)


# ## 4. Model Interpretation
# 
# The Logistic Regression coefficients are examined to identify the customer characteristics most strongly associated with higher or lower predicted churn risk.
# 
# Positive coefficients are associated with increased predicted churn probability, while negative coefficients are associated with reduced predicted churn probability.
# 
# These coefficients describe model associations and should not be interpreted as proof of causation.

# In[22]:


# Extract the fitted preprocessing pipeline

fitted_preprocessor = (

    logistic_model

    .named_steps[
        "preprocessor"
    ]

)


# Extract transformed feature names

feature_names = (

    fitted_preprocessor

    .get_feature_names_out()

)


# Extract Logistic Regression coefficients

model_coefficients = (

    logistic_model

    .named_steps[
        "classifier"
    ]

    .coef_[0]

)


print(
    f"Number of transformed features: "
    f"{len(feature_names)}"
)


print(
    f"Number of model coefficients: "
    f"{len(model_coefficients)}"
)


# In[23]:


# Create a feature-coefficient table

feature_effects = pd.DataFrame(

    {

        "feature": (

            feature_names

        ),

        "coefficient": (

            model_coefficients

        )

    }

)


# Remove preprocessing prefixes

feature_effects[
    "feature"
] = (

    feature_effects[
        "feature"
    ]

    .str.replace(

        "numerical__",

        "",

        regex=False

    )

    .str.replace(

        "categorical__",

        "",

        regex=False

    )

)


# Calculate odds ratios

feature_effects[

    "odds_ratio"

] = np.exp(

    feature_effects[

        "coefficient"

    ]

)


# Add coefficient direction

feature_effects[

    "association"

] = np.where(

    feature_effects[

        "coefficient"

    ] > 0,

    "Higher Predicted Churn",

    "Lower Predicted Churn"

)


# Calculate absolute coefficient strength

feature_effects[

    "absolute_coefficient"

] = (

    feature_effects[

        "coefficient"

    ]

    .abs()

)


feature_effects = (

    feature_effects

    .sort_values(

        "absolute_coefficient",

        ascending=False

    )

    .reset_index(

        drop=True

    )

)


feature_effects.head(20)


# In[24]:


# Select the strongest model associations

top_feature_effects = (

    feature_effects

    .head(16)

    .sort_values(

        "coefficient",

        ascending=True

    )

)


# Create the coefficient chart

fig, ax = plt.subplots(

    figsize=(12, 9)

)


bars = ax.barh(

    top_feature_effects[

        "feature"

    ],

    top_feature_effects[

        "coefficient"

    ]

)


# Add a reference line at zero

ax.axvline(

    x=0,

    linewidth=1.2

)


# Add coefficient labels

for bar, coefficient in zip(

    bars,

    top_feature_effects[

        "coefficient"

    ]

):

    label_position = (

        coefficient + 0.03

        if coefficient >= 0

        else coefficient - 0.03

    )


    alignment = (

        "left"

        if coefficient >= 0

        else "right"

    )


    ax.text(

        label_position,

        bar.get_y()

        + bar.get_height() / 2,

        f"{coefficient:.2f}",

        va="center",

        ha=alignment,

        fontsize=9

    )


# Format the chart

ax.set_title(

    "Strongest Logistic Regression Feature Associations",

    fontsize=16,

    fontweight="bold",

    pad=18

)


ax.set_xlabel(

    "Logistic Regression Coefficient",

    fontsize=12

)


ax.set_ylabel(

    "Model Feature",

    fontsize=12

)


plt.tight_layout()


# Save the chart

feature_effects_chart_path = (

    images_path

    / "14_logistic_regression_feature_effects.png"

)


plt.savefig(

    feature_effects_chart_path,

    dpi=300,

    bbox_inches="tight"

)


plt.show()


print(

    f"Chart saved successfully:\n"

    f"{feature_effects_chart_path}"

)


# In[25]:


# Remove repeated "No internet service" indicators
# from the interpretation chart only

clean_feature_effects = (

    feature_effects.loc[

        ~feature_effects[
            "feature"
        ]

        .str.contains(

            "No internet service",

            case=False,

            na=False

        )

    ]

    .copy()

)


# Select the strongest non-redundant associations

top_clean_feature_effects = (

    clean_feature_effects

    .head(15)

    .sort_values(

        "coefficient",

        ascending=True

    )

)


# Create the cleaner interpretation chart

fig, ax = plt.subplots(

    figsize=(12, 9)

)


bars = ax.barh(

    top_clean_feature_effects[
        "feature"
    ],

    top_clean_feature_effects[
        "coefficient"
    ]

)


ax.axvline(

    x=0,

    linewidth=1.2

)


# Add coefficient labels

for bar, coefficient in zip(

    bars,

    top_clean_feature_effects[
        "coefficient"
    ]

):

    label_position = (

        coefficient + 0.03

        if coefficient >= 0

        else coefficient - 0.03

    )


    alignment = (

        "left"

        if coefficient >= 0

        else "right"

    )


    ax.text(

        label_position,

        bar.get_y()

        + bar.get_height() / 2,

        f"{coefficient:.2f}",

        va="center",

        ha=alignment,

        fontsize=9

    )


ax.set_title(

    "Key Logistic Regression Feature Associations",

    fontsize=16,

    fontweight="bold",

    pad=18

)


ax.set_xlabel(

    "Logistic Regression Coefficient",

    fontsize=12

)


ax.set_ylabel(

    "Model Feature",

    fontsize=12

)


plt.tight_layout()


# Save the cleaner chart

clean_feature_chart_path = (

    images_path

    / "15_key_logistic_regression_features.png"

)


plt.savefig(

    clean_feature_chart_path,

    dpi=300,

    bbox_inches="tight"

)


plt.show()


print(

    f"Chart saved successfully:\n"

    f"{clean_feature_chart_path}"

)


# ## 5. Model Interpretation and Business Recommendations
# 
# ### Model Performance Summary
# 
# The Logistic Regression model was evaluated using an independent testing dataset containing 1,409 customers.
# 
# The model achieved the following results:
# 
# - **Accuracy:** 74.45%
# - **Balanced Accuracy:** 76.03%
# - **Precision for churn:** 51.21%
# - **Recall for churn:** 79.41%
# - **F1-Score:** 62.26%
# - **ROC-AUC:** 85.70%
# 
# The confusion matrix showed that the model:
# 
# - Correctly identified **752 retained customers**.
# - Correctly identified **297 churned customers**.
# - Classified **283 retained customers** as being at risk of churn.
# - Missed **77 customers** who actually churned.
# 
# The model correctly detected approximately **79% of customers who actually churned**.
# 
# This relatively high recall is valuable in a customer-retention setting because failing to identify a customer at genuine risk may result in a lost opportunity to prevent customer loss.
# 
# The model also produced a considerable number of false-positive predictions. These customers did not actually churn but were classified as being at risk.
# 
# The appropriate prediction threshold should therefore depend on:
# 
# - The cost of customer-retention interventions
# - The value of retaining a customer
# - Available retention resources
# - The acceptable balance between identifying more at-risk customers and reducing unnecessary interventions
# 
# The ROC-AUC score of **0.857** indicates that the model demonstrated strong ability to distinguish between customers with higher and lower churn risk.
# 
# ---
# 
# ### Key Model Associations
# 
# The final Logistic Regression coefficient analysis identified several customer characteristics associated with higher or lower predicted churn risk after accounting for the other variables included in the model.
# 
# Positive coefficients indicate an association with higher predicted churn probability.
# 
# Negative coefficients indicate an association with lower predicted churn probability.
# 
# These relationships represent statistical associations and should not be interpreted as evidence of direct causation.
# 
# ---
# 
# ### Factors Associated with Higher Predicted Churn
# 
# The strongest positive model associations included:
# 
# #### Month-to-Month Contracts
# 
# Month-to-month contracts showed the strongest positive contract-related association with predicted churn.
# 
# This result was consistent with the exploratory analysis, where month-to-month customers recorded a churn rate of **42.71%**.
# 
# Customers with flexible monthly contracts may have fewer barriers to switching providers and may therefore require stronger retention efforts.
# 
# #### Fiber Optic Internet Service
# 
# Fiber optic service was associated with higher predicted churn after accounting for the other model variables.
# 
# The exploratory analysis also showed that fiber optic customers recorded a churn rate of **41.89%**.
# 
# This result does not indicate that fiber optic technology causes churn. Possible contributing factors may include:
# 
# - Higher monthly charges
# - Service expectations
# - Reliability concerns
# - Competitive offers
# - Differences in customer profiles
# 
# #### Paperless Billing
# 
# Paperless billing showed a moderate positive association with predicted churn.
# 
# However, this variable should be interpreted carefully because customers using paperless billing may also differ in contract type, internet service, payment method, and monthly charges.
# 
# #### Electronic Check Payment
# 
# Electronic check payment showed a positive association with predicted churn.
# 
# This result was consistent with the exploratory analysis, where electronic check customers recorded the highest payment-method churn rate at **45.29%**.
# 
# Electronic check users may represent an important customer group for targeted payment-conversion programs.
# 
# #### Total Charges
# 
# Total charges showed a positive conditional coefficient after accounting for customer tenure, monthly charges, contract type, services, and other model variables.
# 
# This result should not be interpreted independently because total charges are strongly related to customer tenure and monthly spending.
# 
# ---
# 
# ### Factors Associated with Lower Predicted Churn
# 
# The strongest negative model associations included:
# 
# #### Having Dependents
# 
# Having dependents showed the largest negative model coefficient.
# 
# Customers with dependents also recorded substantially lower churn during the exploratory analysis.
# 
# This relationship may reflect greater household stability, longer customer relationships, or differences in contract and service usage.
# 
# #### Longer Customer Tenure
# 
# Longer customer tenure showed a strong negative association with predicted churn.
# 
# This result was consistent with the exploratory analysis:
# 
# - Customers within their first 0–6 months recorded a churn rate of **52.94%**.
# - Customers with more than 49 months of tenure recorded a churn rate of only **9.51%**.
# 
# Customer tenure appears to be one of the strongest indicators of customer stability.
# 
# #### Two-Year Contracts
# 
# Two-year contracts showed a strong negative association with predicted churn.
# 
# The exploratory analysis showed that two-year customers recorded a churn rate of only **2.83%**.
# 
# Long-term contractual commitment was therefore associated with stronger customer retention.
# 
# #### DSL Internet Service
# 
# DSL service showed a lower predicted churn association compared with other modeled internet-service categories.
# 
# The exploratory analysis also showed a lower churn rate among DSL customers than fiber optic customers.
# 
# #### No Internet Service
# 
# Customers without internet service showed a lower predicted churn association within this dataset.
# 
# This relationship may reflect lower service complexity, lower monthly charges, or differences in customer needs.
# 
# ---
# 
# ### Interpretation Considerations
# 
# Logistic Regression coefficients represent conditional associations while holding the other modeled variables constant.
# 
# They should not be interpreted as evidence that a specific feature directly causes customer churn.
# 
# The numerical variables were standardized before model training.
# 
# Therefore, the coefficients and odds ratios of numerical features represent the estimated effect associated with approximately a one-standard-deviation increase rather than a one-unit increase.
# 
# Monthly charges, total charges, tenure, contract type, and internet-service type are strongly related.
# 
# Their coefficients should therefore be interpreted jointly rather than used independently to make direct pricing conclusions.
# 
# The model produced:
# 
# - A negative coefficient for monthly charges
# - A positive coefficient for total charges
# 
# This does not mean that higher monthly charges directly reduce churn.
# 
# These coefficients reflect conditional relationships after accounting for customer tenure, contract type, service usage, and the other variables included in the model.
# 
# Partner status showed a positive model coefficient even though customers with partners recorded a lower churn rate during the descriptive analysis.
# 
# This difference may occur because the multivariable model estimates the relationship of partner status after accounting for:
# 
# - Customer tenure
# - Dependents
# - Contract type
# - Services
# - Payment behavior
# - Other customer characteristics
# 
# Repeated service indicators related to customers without internet access were removed from the final feature-association visualization to reduce redundancy.
# 
# The underlying Logistic Regression model was not changed.
# 
# ---
# 
# ## Business Recommendations
# 
# ### 1. Prioritize the Early Customer Lifecycle
# 
# Customers within their first six months recorded the highest observed churn rate.
# 
# The company should implement a structured early-retention program that includes:
# 
# - Guided onboarding
# - Welcome communications
# - Early satisfaction surveys
# - Proactive service checks
# - Technical-support follow-up
# - Customer education about available services
# 
# Retention interventions should be concentrated during the first six months because this period showed the highest customer-loss risk.
# 
# ---
# 
# ### 2. Develop Contract-Conversion Offers
# 
# Month-to-month customers represented the largest concentration of customer churn.
# 
# The company could test targeted incentives that encourage suitable customers to move toward longer-term agreements.
# 
# Potential offers may include:
# 
# - Discounts for annual contracts
# - Loyalty benefits
# - Service upgrades
# - Bundled support services
# - Contract-renewal rewards
# 
# These programs should be evaluated carefully to ensure that the expected retention benefit exceeds the cost of the incentive.
# 
# ---
# 
# ### 3. Encourage Automatic Payment Adoption
# 
# Electronic check users and manual-payment customers showed elevated churn during the exploratory analysis.
# 
# The company could test incentives that encourage suitable customers to adopt automatic bank-transfer or credit-card payments.
# 
# Potential actions may include:
# 
# - Small automatic-payment discounts
# - Loyalty benefits
# - Simplified payment enrollment
# - Automatic-payment reminders during onboarding
# - Payment-method education
# 
# The impact of these initiatives should be tested before large-scale implementation.
# 
# ---
# 
# ### 4. Build a High-Risk Customer Retention Workflow
# 
# Customers with high predicted churn probabilities should be prioritized according to both churn risk and customer value.
# 
# A retention workflow could include:
# 
# 1. Generate updated customer churn probabilities.
# 2. Rank customers by predicted risk.
# 3. Combine predicted risk with customer lifetime value.
# 4. Prioritize high-value customers with elevated churn risk.
# 5. Assign appropriate retention actions.
# 6. Track intervention results.
# 
# Potential retention actions include:
# 
# - Proactive customer-service outreach
# - Personalized retention offers
# - Contract-upgrade incentives
# - Technical-support assistance
# - Service-quality follow-up
# - Customized loyalty benefits
# 
# The prediction threshold should be selected according to retention costs and available business resources.
# 
# ---
# 
# ### 5. Review the Fiber Optic Customer Experience
# 
# Fiber optic customers showed elevated churn in both the exploratory analysis and the predictive model.
# 
# The company should investigate:
# 
# - Service reliability
# - Network performance
# - Monthly pricing
# - Customer expectations
# - Complaint frequency
# - Competitor offerings
# - Service-value perception
# 
# Fiber optic customers should not automatically receive discounts.
# 
# The company should first identify whether churn is primarily associated with price, service quality, competition, customer expectations, or a combination of these factors.
# 
# ---
# 
# ### 6. Strengthen Technical Support and Online Security Adoption
# 
# Customers without technical support or online security recorded substantially higher observed churn rates.
# 
# The company could evaluate bundled packages that combine:
# 
# - Technical support
# - Online security
# - Device protection
# - Customer education
# 
# These services may increase perceived value and improve the overall customer experience.
# 
# However, their effect should be tested through controlled retention initiatives before being interpreted as causal.
# 
# ---
# 
# ### 7. Improve Service and Support Quality
# 
# Service and support issues represented a major share of reported churn reasons.
# 
# The company should strengthen:
# 
# - Customer-service training
# - Response-time monitoring
# - Complaint-resolution procedures
# - Escalation processes
# - Customer-feedback collection
# - Service-quality measurement
# 
# The attitude of support staff was the most frequently reported individual churn reason.
# 
# This finding suggests that customer interactions may play an important role in retention.
# 
# ---
# 
# ### 8. Monitor Competitive Pressure
# 
# Competitor-related reasons represented the largest reported churn category at **33.23%**.
# 
# The company should regularly benchmark:
# 
# - Competitor pricing
# - Download speeds
# - Data allowances
# - Device offerings
# - Promotional campaigns
# - Contract conditions
# - Service bundles
# 
# Competitive intelligence should be connected with customer-risk monitoring so that vulnerable customer segments can receive timely and relevant retention offers.
# 
# ---
# 
# ## Final High-Risk Customer Profile
# 
# The combined exploratory and predictive analysis suggests that customers with several of the following characteristics may require additional retention attention:
# 
# - Short customer tenure
# - Month-to-month contract
# - Fiber optic internet service
# - No technical support
# - No online security
# - Electronic check payment
# - Manual payment behavior
# - Higher observed service costs
# - Limited long-term customer commitment
# 
# No single factor should be used independently to determine customer risk.
# 
# Retention decisions should combine:
# 
# - Predicted churn probability
# - Customer lifetime value
# - Customer service history
# - Contract information
# - Available retention resources
# 
# ---
# 
# ## Model Limitations
# 
# The following limitations should be considered when interpreting the results:
# 
# - The analysis identifies statistical associations rather than causal relationships.
# - The model was evaluated using one stratified train-test split.
# - The dataset may not represent current customer behavior in every telecommunications market.
# - Logistic Regression primarily captures linear relationships in the transformed feature space.
# - The classification threshold remained at the default value of **0.50**.
# - The prediction threshold was not optimized using retention costs or customer lifetime value.
# - Model probabilities were not formally calibrated.
# - External validation was not performed.
# - Some customer characteristics may interact in ways that are not fully captured by Logistic Regression.
# 
# Future work could:
# 
# - Compare Logistic Regression with tree-based models
# - Apply cross-validation
# - Evaluate probability calibration
# - Optimize the prediction threshold
# - Incorporate retention costs
# - Use customer lifetime value in decision rules
# - Evaluate model stability over time
# - Test the model on new customer data

# ## 6. Model Saving and Customer Risk Outputs
# 
# The evaluated model, final full-data model, customer-level predictions, churn-risk scores, and model metadata are saved as reusable project artifacts.
# 
# The reported evaluation metrics remain based on the independent testing dataset. After the evaluation approach was finalized, a separate final model was trained using all available labeled data for future customer scoring.

# In[26]:


# Import model-saving and metadata tools

import json
import joblib

from sklearn.base import clone


# Define the main project path

project_path = Path(
    r"C:\Users\hp15-da\Desktop\معرض عمال\Customer_Churn_Intelligence"
)


# Define model and output folders

models_path = (
    project_path
    / "models"
)


outputs_path = (
    project_path
    / "outputs"
)


# Create folders if they do not already exist

models_path.mkdir(
    parents=True,
    exist_ok=True
)


outputs_path.mkdir(
    parents=True,
    exist_ok=True
)


print(
    "Model and output folders created successfully."
)


# In[27]:


# Save the evaluated model trained on the training subset

evaluated_model_path = (

    models_path

    / "logistic_regression_evaluated.joblib"

)


joblib.dump(

    logistic_model,

    evaluated_model_path

)


print(
    "Evaluated model saved successfully."
)


print(
    evaluated_model_path
)


# In[28]:


# Create a new final model using the validated pipeline

final_logistic_model = clone(

    logistic_model

)


# Train the final model using all available labeled data

final_logistic_model.fit(

    X,

    y

)


# Define the final model path

final_model_path = (

    models_path

    / "logistic_regression_final.joblib"

)


# Save the final full-data model

joblib.dump(

    final_logistic_model,

    final_model_path

)


print(
    "Final full-data model trained and saved successfully."
)


print(
    final_model_path
)


# In[29]:


# Create customer-level predictions for the testing dataset

test_predictions = (

    df.loc[

        X_test.index,

        [

            "customer_id",

            "tenure_months",

            "contract",

            "internet_service",

            "payment_method",

            "monthly_charges",

            "cltv"

        ]

    ]

    .copy()

)


# Add actual and predicted outcomes

test_predictions[

    "actual_churn"

] = (

    y_test

)


test_predictions[

    "predicted_churn"

] = (

    y_pred

)


test_predictions[

    "churn_probability"

] = (

    y_pred_probability

)


# Create business-friendly risk segments

test_predictions[

    "risk_segment"

] = pd.cut(

    test_predictions[

        "churn_probability"

    ],

    bins=[

        -0.001,

        0.25,

        0.50,

        0.75,

        1.00

    ],

    labels=[

        "Low Risk",

        "Moderate Risk",

        "High Risk",

        "Very High Risk"

    ],

    include_lowest=True

)


# Sort customers from highest to lowest predicted risk

test_predictions = (

    test_predictions

    .sort_values(

        "churn_probability",

        ascending=False

    )

    .reset_index(

        drop=True

    )

)


# Round probabilities

test_predictions[

    "churn_probability"

] = (

    test_predictions[

        "churn_probability"

    ]

    .round(4)

)


# Save the testing predictions

test_predictions_path = (

    outputs_path

    / "test_set_churn_predictions.csv"

)


test_predictions.to_csv(

    test_predictions_path,

    index=False,

    encoding="utf-8-sig"

)


print(
    "Testing predictions saved successfully."
)


print(

    f"Number of customers: "

    f"{len(test_predictions):,}"

)


test_predictions.head(10)


# In[30]:


# Generate churn predictions for all customers
# using the final full-data model

all_customer_predictions = (

    final_logistic_model

    .predict(

        X

    )

)


all_customer_probabilities = (

    final_logistic_model

    .predict_proba(

        X

    )

    [:, 1]

)


# Create the complete customer-risk output

all_customer_risk_scores = (

    df[

        [

            "customer_id",

            "tenure_months",

            "contract",

            "internet_service",

            "tech_support",

            "online_security",

            "payment_method",

            "monthly_charges",

            "cltv",

            "churn_value"

        ]

    ]

    .copy()

)


all_customer_risk_scores[

    "predicted_churn"

] = (

    all_customer_predictions

)


all_customer_risk_scores[

    "churn_probability"

] = (

    all_customer_probabilities

)


# Create customer-risk segments

all_customer_risk_scores[

    "risk_segment"

] = pd.cut(

    all_customer_risk_scores[

        "churn_probability"

    ],

    bins=[

        -0.001,

        0.25,

        0.50,

        0.75,

        1.00

    ],

    labels=[

        "Low Risk",

        "Moderate Risk",

        "High Risk",

        "Very High Risk"

    ],

    include_lowest=True

)


# Rank customers by predicted churn risk

all_customer_risk_scores = (

    all_customer_risk_scores

    .sort_values(

        "churn_probability",

        ascending=False

    )

    .reset_index(

        drop=True

    )

)


# Round predicted probabilities

all_customer_risk_scores[

    "churn_probability"

] = (

    all_customer_risk_scores[

        "churn_probability"

    ]

    .round(4)

)


# Save all customer-risk scores

all_customer_scores_path = (

    outputs_path

    / "all_customer_churn_risk_scores.csv"

)


all_customer_risk_scores.to_csv(

    all_customer_scores_path,

    index=False,

    encoding="utf-8-sig"

)


print(
    "All customer-risk scores saved successfully."
)


print(

    f"Number of customers: "

    f"{len(all_customer_risk_scores):,}"

)


all_customer_risk_scores.head(10)


# In[31]:


# Create reusable model metadata

model_metadata = {

    "project_name": (

        "Customer Churn Intelligence"

    ),

    "model_name": (

        "Logistic Regression"

    ),

    "target_variable": (

        "churn_value"

    ),

    "classification_threshold": (

        0.50

    ),

    "training_strategy": (

        "Stratified 80/20 train-test split"

    ),

    "test_size": (

        0.20

    ),

    "random_state": (

        42

    ),

    "class_weight": (

        "balanced"

    ),

    "evaluation_metrics": {

        "accuracy": (

            round(

                float(accuracy),

                4

            )

        ),

        "balanced_accuracy": (

            round(

                float(

                    balanced_accuracy

                ),

                4

            )

        ),

        "precision": (

            round(

                float(precision),

                4

            )

        ),

        "recall": (

            round(

                float(recall),

                4

            )

        ),

        "f1_score": (

            round(

                float(f1),

                4

            )

        ),

        "roc_auc": (

            round(

                float(roc_auc),

                4

            )

        )

    },

    "confusion_matrix": {

        "true_negatives": (

            int(

                true_negatives

            )

        ),

        "false_positives": (

            int(

                false_positives

            )

        ),

        "false_negatives": (

            int(

                false_negatives

            )

        ),

        "true_positives": (

            int(

                true_positives

            )

        )

    },

    "numerical_features": (

        numerical_features

    ),

    "categorical_features": (

        categorical_features

    ),

    "excluded_columns": (

        columns_to_exclude

    ),

    "saved_model_files": [

        "logistic_regression_evaluated.joblib",

        "logistic_regression_final.joblib"

    ],

    "notes": (

        "Evaluation metrics were calculated "

        "using the independent testing dataset. "

        "The final model was retrained using all "

        "available labeled data after the model "

        "evaluation approach was finalized."

    )

}


# Define metadata path

metadata_path = (

    outputs_path

    / "model_metadata.json"

)


# Save metadata as JSON

with open(

    metadata_path,

    "w",

    encoding="utf-8"

) as metadata_file:

    json.dump(

        model_metadata,

        metadata_file,

        indent=4,

        ensure_ascii=False

    )


print(
    "Model metadata saved successfully."
)


print(
    metadata_path
)


# In[32]:


# Verify all saved model artifacts

saved_artifacts = [

    evaluated_model_path,

    final_model_path,

    test_predictions_path,

    all_customer_scores_path,

    metadata_path

]


artifact_status = pd.DataFrame(

    {

        "artifact": [

            path.name

            for path

            in saved_artifacts

        ],

        "exists": [

            path.exists()

            for path

            in saved_artifacts

        ]

    }

)


artifact_status


# In[ ]:




