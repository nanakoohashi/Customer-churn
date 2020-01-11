# Exploratory Analysis

## Importing the Libraries
# import all packages and set plots to be embedded inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import show
import seaborn as sns
%matplotlib inline
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import (train_test_split, GridSearchCV, RandomizedSearchCV)
from sklearn.metrics import (roc_auc_score, roc_curve, classification_report)
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import (GradientBoostingClassifier,RandomForestClassifier)
from scipy import stats
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

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
# check duplicates within data set
sum(df.duplicated())
# check null entries within data set
df.isnull().sum()
# Count how many churners and non-churners the dataset contains. 
df['Churn'].value_counts()
"""This dataset has 7,043 samples, and 21 attributes(2 integers, 1 float, and 18 objects).
No variable column has null/missing values.
Discuss each column here:
- `customerID` - contains random values and has no effect on customer leaving telecommunications company.
- `gender` - may play a role in a customer leaving the company. This column will be included.
- `SeniorCitizen` - may play a role in a customer leaving the company. This column will be included.
- `Partner` - may play a role in a customer leaving the company. This column will be included.
- `Dependents` - may play a role in a customer leaving the company. This column will be included.
- `tenure` - refers to the number of years the customer has been a client of the company. It may play a role in a customer leaving the company. This column will be included.
- `PhoneService` - may play a role in a customer leaving the company. This column will be included.
- `MultipleLines` - may play a role in a customer leaving the company. This column will be included.
- `InternetService` - may play a role in a customer leaving the company. This column will be included.
- `OnlineSecurity` - may play a role in a customer leaving the company. This column will be included.
- `OnlineBackup` - may play a role in a customer leaving the company. This column will be included.
- `DeviceProtection` - may play a role in a customer leaving the company. This column will be included.
- `TechSupport` - may play a role in a customer leaving the company. This column will be included.
- `StreamingTV` - may play a role in a customer leaving the company. This column will be included.
- `StreamingMovies` - may play a role in a customer leaving the company. This column will be included.
- `Contract` - may play a role in a customer leaving the company. This column will be included.
- `PaperlessBilling` - may play a role in a customer leaving the company. This column will be included.
- `PaymentMethod` - may play a role in a customer leaving the company. This column will be included.
- `MonthlyCharges` - may play a role in a customer leaving the company. This column will be included.
- `TotalCharges` - may play a role in a customer leaving the company. This column will be included.
- `Churn` - whether or not the customer has left the company. This is what I will be predicting.
## Issues
- We have some non-numeric data"""

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
# Total charges contain entries that are not floats. Use ‘coerce’ - invalid parsing will be set as NaN
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors = 'coerce')
df.loc[df['TotalCharges'].isna()==True]
# `tenure = 0` for `TotalCharges` columns. Convert TotalCharges to 0 for these entries.
df[df['TotalCharges'].isna()==True] = 0
# Unique values for categorical column entries
df.gender.unique()
df.Partner.unique()
df.Dependents.unique()
df.PhoneService.unique()
df.MultipleLines.unique()
df.InternetService.unique()
df.OnlineSecurity.unique()
df.OnlineBackup.unique()
df.DeviceProtection.unique()
df.TechSupport.unique()
df.StreamingTV.unique()
df.StreamingMovies.unique()
df.Contract.unique()
df.PaperlessBilling.unique()
df.PaymentMethod.unique()
df.Churn.unique()
# convert categorical values into numerical values
df.gender.replace(['Male','Female'],[0,1], inplace=True)
df.Partner.replace(['No', 'Yes'],[0,1], inplace=True)
df.Dependents.replace(['Yes','No'],[1,0], inplace=True)
df.PhoneService.replace(['No', 'Yes'],[0,1], inplace=True)
df.MultipleLines.replace(['No phone service','No', 'Yes'], [0,0,1], inplace=True)
df.InternetService.replace(['No', 'DSL', 'Fiber optic'], [0,1,2], inplace=True)
df.OnlineSecurity.replace(['No internet service','No', 'Yes'], [0,0,1], inplace=True)
df.OnlineBackup.replace(['No internet service','No', 'Yes'], [0,0,1], inplace=True)
df.DeviceProtection.replace(['No internet service','No', 'Yes'], [0,0,1], inplace=True)
df.TechSupport.replace(['No internet service','No', 'Yes'], [0,0,1], inplace=True)
df.StreamingTV.replace(['No internet service','No', 'Yes'], [0,0,1], inplace=True)
df.StreamingMovies.replace(['No internet service','No', 'Yes'], [0,0,1], inplace=True)
df.Contract.replace(['Month-to-month','One year', 'Two year'], [0,1,2], inplace=True)
df.PaperlessBilling.replace(['No', 'Yes'], [0,1], inplace=True)
df.PaymentMethod.replace(['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], [1,2,3,4], inplace=True)
df.Churn.replace(['No', 'Yes'], [0,1], inplace=True)

## Legend
"""- `gender`: Male = 0, Female = 1
- `SeniorCitizen`: No = 0, Yes = 1
- `Partner`: No = 0, Yes = 1
- `Dependents`: No = 0, Yes = 1
- `tenure`: # months
- `PhoneService`: No = 0, Yes = 1
- `MultipleLines`: No = 0, Yes = 1
- `InternetService`: No = 0, DSL = 1, Fiber optic = 2
- `OnlineSecurity`: No = 0, Yes = 1
- `OnlineBackup`: No = 0, Yes = 1
- `DeviceProtection`: No = 0, Yes = 1
- `TechSupport`: No = 0, Yes = 1
- `StreamingTV`: No = 0, Yes = 1
- `StreamingMovies`: No = 0, Yes = 1
- `Contract`: Month-to-month = 0, One year = 1, Two year = 2
- `PaperlessBilling`: No = 0, Yes = 1
- `PaymentMethod`: None = 0, Electronic check = 1, Mailed check = 2, Bank transfer (automatic) = 3, Credit Card (automatic) = 4
- `Churn`: No = 0, Yes = 1"""

# Drop Customer ID column
df = df.drop(['customerID'], axis = 1)
df.info()

# Group df by 'Churn' and compute the mean
df.groupby(['Churn']).mean()
# Group df by 'Churn' and compute the standard deviation
df.groupby(['Churn']).std()
df.describe()
# Data Visualization
sns.countplot(data = df, x = 'Churn')
plt.title('Distribution of Churn')
plt.ylabel('Frequency')
plt.xlabel('Churn')
# Calculate Churn Percentage
churn_True = df["Churn"][df["Churn"] == True]
print ("Churn Percentage = "+ str( (churn_True.shape[0] / df["Churn"].shape[0]) * 100 ) +("%"))
# Univariate Exploration
## Continuous Variables
df.hist(column = 'MonthlyCharges', bins=20, figsize=(8,4))
plt.show()
df.hist(column = 'TotalCharges', bins=20, figsize=(8,4))
plt.show()
df.hist(column = 'tenure', bins=20, figsize=(8,4))
plt.show()
## Categorical Variables
sns.countplot(x = 'gender', data = df)
sns.countplot(x = 'SeniorCitizen', data = df)
sns.countplot(x = 'Partner', data = df)
sns.countplot(x = 'Dependents', data = df)
sns.countplot(x = 'PhoneService', data = df)
sns.countplot(x = 'MultipleLines', data = df)
sns.countplot(x = 'InternetService', data = df)
sns.countplot(x = 'OnlineSecurity', data = df)
sns.countplot(x = 'OnlineBackup', data = df)
sns.countplot(x = 'DeviceProtection', data = df)
sns.countplot(x = 'TechSupport', data = df)
sns.countplot(x = 'StreamingTV', data = df)
sns.countplot(x = 'StreamingMovies', data = df)
sns.countplot(x = 'Contract', data = df)
sns.countplot(x = 'PaperlessBilling', data = df)
sns.countplot(x = 'PaymentMethod', data = df)

# Bivariate Exploration
## Explore relationships with each variable and churn
# heatmap
corr = df.corr()
sns.heatmap(corr, xticklabels = corr.columns.values, yticklabels = corr.columns.values, annot = True)
heat_map = plt.gcf()
heat_map.set_size_inches(18,14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()
sns.countplot(data = df, x = 'gender', hue = 'Churn')
sns.countplot(data = df, x = 'SeniorCitizen', hue = 'Churn')
sns.countplot(data = df, x = 'Partner', hue = 'Churn')
sns.countplot(data = df, x = 'Dependents', hue = 'Churn')
# Group all continuous variables
numeric = df[['tenure', 'MonthlyCharges', 'TotalCharges']]
# Plot continuous variables against churn
numeric = pd.concat([numeric, df["Churn"]],axis=1) #Add the 'Churn' variable to the numeric dataset
g = sns.PairGrid(numeric.sample(n=1000), hue="Churn")
g = g.map_offdiag(plt.scatter, linewidths=1, edgecolor="w", s=40)
g = g.map_diag(sns.kdeplot)
g = g.add_legend()
sns.countplot(data = df, x = 'PhoneService', hue = 'Churn')
sns.countplot(data = df, x = 'MultipleLines', hue = 'Churn')
sns.countplot(data = df, x = 'InternetService', hue = 'Churn')
sns.countplot(data = df, x = 'OnlineSecurity', hue = 'Churn')
sns.countplot(data = df, x = 'OnlineBackup', hue = 'Churn')
sns.countplot(data = df, x = 'DeviceProtection', hue = 'Churn')
sns.countplot(data = df, x = 'TechSupport', hue = 'Churn')
sns.countplot(data = df, x = 'StreamingTV', hue = 'Churn')
