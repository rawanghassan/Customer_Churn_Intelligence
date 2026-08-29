#!/usr/bin/env python
# coding: utf-8

# # Customer Churn Intelligence
# 
# ## Exploratory Data Analysis
# 
# This notebook analyzes customer behavior, churn patterns, service usage, payment methods, and customer risk indicators using the cleaned Telco Customer Churn dataset.
# 
# ### Project Objectives
# 
# - Understand the overall customer churn rate.
# - Identify customer groups with higher churn risk.
# - Analyze churn across contracts, services, tenure, and payment methods.
# - Generate business-focused insights and retention recommendations.

# In[ ]:





# In[2]:


# Import the required libraries

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Improve table display inside Jupyter

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 100)
pd.set_option("display.float_format", "{:,.2f}".format)


# Set a clean chart theme

sns.set_theme(
    style="whitegrid",
    context="notebook"
)


print("Libraries imported successfully.")


# In[6]:


# Define the exact path to the cleaned dataset

from pathlib import Path

data_path = Path(
    r"C:\Users\hp15-da\Desktop\معرض عمال\Customer_Churn_Intelligence\data\telco_customer_churn_clean.csv"
)


# Check that the file exists

print("File exists:", data_path.exists())


# Load the cleaned dataset

df = pd.read_csv(
    data_path,
    encoding="utf-8"
)


print("Dataset loaded successfully.")
print(f"Number of rows: {df.shape[0]:,}")
print(f"Number of columns: {df.shape[1]}")


# In[7]:


# Preview the first five customer records

df.head()


# In[ ]:




