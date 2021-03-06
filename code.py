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
sns.countplot(data = df, x = 'StreamingMovies', hue = 'Churn')
sns.countplot(data = df, x = 'Contract', hue = 'Churn')
sns.countplot(data = df, x = 'PaperlessBilling', hue = 'Churn')
sns.countplot(data = df, x = 'PaymentMethod', hue = 'Churn')
sns.regplot(data = df, x = 'tenure', y = 'MonthlyCharges')
sns.regplot(data = df, x = 'tenure', y = 'TotalCharges')
sns.regplot(data = df, x = 'MonthlyCharges', y = 'TotalCharges')

# Feature Selection
from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
X = df[['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
        'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']]
y = df.Churn
model.fit(X,y)
print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
#plot graph of feature importances for better visualization
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(10).plot(kind='barh')
plt.title('Which Features Affect Churn the Most?')
plt.show()
"""Observations
The features that have the most importance are:

tenure
TotalCharges
MonthlyCharges
Payment Method
Contract
InternetService
We will disregard the other categories for the rest of the analysis."""
df2 = df[['tenure', 'TotalCharges', 'MonthlyCharges', 'InternetService', 'PaymentMethod', 'Contract', 'Churn']]
# Detecting Multicollinearity
X = add_constant(df2)
>>> pd.Series([variance_inflation_factor(X.values, i) 
               for i in range(X.shape[1])], 
              index=X.columns)
"""If VIF > 10, then multicollinearity is high.

Ignore columns with dummy variables with high VIFs - If you have high VIFs for dummy variables representing nominal variables with three or more categories, those are usually not a problem (Statistics How To, 2015).

We will remove MonthlyCharges from the analysis."""
df3 = df2[['tenure', 'TotalCharges', 'InternetService', 'PaymentMethod', 'Contract', 'Churn']]
# Check if there is any highly correlated variables remaining
X = add_constant(df3)
pd.Series([variance_inflation_factor(X.values, i) 
               for i in range(X.shape[1])], 
              index=X.columns)
# Descriptive Method - PCA
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)
x_pca 
x_pca_df = pd.DataFrame(data = x_pca, columns = ['principal component 1', 'principal component 2'])
x_pca_df.tail()
print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))
scaled_data.shape
x_pca.shape
plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=df3['Churn'], cmap='rainbow')
plt.xlabel('First principal component')
plt.ylabel('Second Principal Component')
pca.components_
map= pd.DataFrame(pca.components_,columns=df.columns)
plt.figure(figsize=(12,6))
sns.heatmap(map,cmap='twilight')

# Predictive Analysis - Logistic Regression
from sklearn.model_selection import train_test_split
train, test = train_test_split(df3, test_size = 0.25)
 
train_y = train['Churn']
test_y = test['Churn']
 
train_x = train
train_x.pop('Churn')
test_x = test
test_x.pop('Churn')
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
 
logisticRegr = LogisticRegression()
logisticRegr.fit(X=train_x, y=train_y)
 
test_y_pred = logisticRegr.predict(test_x)
confusion_matrix = confusion_matrix(test_y, test_y_pred)
print('Intercept: ' + str(logisticRegr.intercept_))
print('Regression: ' + str(logisticRegr.coef_))
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logisticRegr.score(test_x, test_y)))
print(classification_report(test_y, test_y_pred))
 
confusion_matrix_df = pd.DataFrame(confusion_matrix, ('No churn', 'Churn'), ('No churn', 'Churn'))
heatmap = sns.heatmap(confusion_matrix_df, annot=True, annot_kws={"size": 20}, fmt="d")
heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize = 14)
heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right', fontsize = 14)
plt.ylabel('True label', fontsize = 14)
plt.xlabel('Predicted label', fontsize = 14)

print(logisticRegr.coef_)

feat_importances = pd.Series(logisticRegr.coef_[0], index=train.columns)
feat_importances.nlargest(10).plot(kind='barh')

df.Churn.value_counts()

## Up-sampling the minority class
from sklearn.utils import resample

data_majority = df3[df3['Churn']==0]
data_minority = df3[df3['Churn']==1]

data_minority_upsampled = resample(data_minority,
replace=True,
n_samples=4653, #same number of samples as majority class
random_state=1) #set the seed for random resampling
# Combine resampled results
data_upsampled = pd.concat([data_majority, data_minority_upsampled])

data_upsampled['Churn'].value_counts()

train, test = train_test_split(data_upsampled, test_size = 0.25)

train_y_upsampled = train['Churn']
test_y_upsampled = test['Churn']

train_x_upsampled = train
train_x_upsampled.pop('Churn')
test_x_upsampled = test
test_x_upsampled.pop('Churn')

logisticRegr_balanced = LogisticRegression()
logisticRegr_balanced.fit(X=train_x_upsampled, y=train_y_upsampled)

test_y_pred_balanced = logisticRegr_balanced.predict(test_x_upsampled)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logisticRegr_balanced.score(test_x_upsampled, 
                                                                                                          test_y_upsampled)))
print(classification_report(test_y_upsampled, test_y_pred_balanced))

logisticRegr2= LogisticRegression()
logisticRegr2.fit(X=train_x_upsampled, y=train_y_upsampled)
feat_importances = pd.Series(logisticRegr2.coef_[0], index=train.columns)
feat_importances.nlargest(10).plot(kind='barh')

#The overall accuracy has decreased, but the precision and recall scores for predicting a churn have increased.

# Tree-Based Algorithms - Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=200, random_state=0)
classifier.fit(train_x, train_y)
predictions = classifier.predict(test_x)

from sklearn.metrics import classification_report, accuracy_score
print(classification_report(test_y, predictions))  
print(accuracy_score(test_y, predictions))

classifier.feature_importances_

X.columns

train.columns

feat_importances = pd.Series(classifier.feature_importances_, index=train.columns)
feat_importances.nlargest(10).plot(kind='barh')
