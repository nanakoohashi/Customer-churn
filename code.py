# Import all packagees and set plots to be embedded inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
%matplotlib inline

# Data Wrangling (Data Munging)
# load Customer Data dataset into a pandas dataframe
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

df.head()
print(df.shape)


# check data types of each column
df.dtypes
