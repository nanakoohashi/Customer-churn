# Import all packagees and set plots to be embedded inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
%matplotlib inline

# load Customer Data dataset into a pandas dataframe

# Data Wrangling (Data Munging)
# General Properties
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
# visually assess the data set
df.head()
# shape of data set
print(df.shape)
# summary
df.info()
# check data types of each column
df.dtypes
# Count how many churners and non-churners the dataset contains. 
df['Churn'].value_counts()
# Model Outcomes
## Two classes:
### yes = Customer will churn.
### no = Customer will not churn.
# Exploratory Analysis
## Differences between churners and non-churners
### Do churners call customer service more often?
### Does one state have more churners compared to another?
## Grouping and summarizing data
### .groupby()
# Group df by 'Churn' and compute the mean
df.groupby(['Churn']).mean()
df.groupby(['Churn']).median()
# Group df by 'Churn' and compute the standard deviation
df.groupby(['Churn']).std()
