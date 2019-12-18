# Data Mining and Analytics Plan
## 1. Define the Business Obejctives
## 2. Assess the Business Environment for Data Mining
## 3. Formulate the Analytical Goals and Objectives of the Project
- Build a suitable database, for easy extraction for modeling data sets.
- Develop and deploy a model which generates significant value
- Build a knowledge base for modeling "learnings", to increase efficiency of data mining process (e.g. to make it cheaper, faster, and easier).
### Objectives
  - Acquiring a suitable data set for modeling
  - Creating a short list of predictor variables
  - Creating a model of acceptable accuracy
  - Monitoring for acceptqable performance
  - Updating model with current data
  - Providing feedback of intelligence gained by application of the model.
### Tasks
  - Identification/derivation of the target variable (the variable to be predicted)
  - Univariate and bivariate analysis of candidate predictor variables
  - Multivariate analysiis of candidate predictor variables
  - Correlation analysis of candidate predictor variables
  - Preliminary screening of variables with various metrics and screening algorithms (e. g. GINI scoring or some measure of "interestingness".
  - Preliminary modeling of the target variable (e.g. with a decision tree algorithm) to select variables for the short list.
### Subtasks/Steps
  - Generation of various decriptive statistics (e.g. means and standard deviations)
  - Bivariate scatterplots
  - Association and linkage analysis.
## Data Understanding
### 1. Data acquisition
- Data access
  - Find and extract the right data for modeling.
- Data integration
  - Combine data sets.
  - Data in relational databases must either be flattened (gathered together into one row or record), or the data map must be traversed to access the data in the databases directly through in-database access utilities, available in some analytic tools.
  - In addition to extraction, may field s of data must be transformed and new variables derived.
- Initial data collection report
### 2. Data Description
- Variables
- Cases
- Descriptive Statistics
- Data Description Report
### 3. Data Quality Assessment
- Missing values
- Outliers
- Data quality report
## Data Preparation
- Data cleansing: clean data
- Data transportation: express data variables
- Data imputation: handle missing values
- Data weighting and balancing: are all cases treated the same?
- Data filtering: do something about outliers and other unwanted data
- Data abstraction: handle temporal (time-series) data
- Data reduction: reduce the amount of data to use
- Data sampling: records
- Dimensionality reduction: variables
- Data discretization: values
- Data derivation: create new variables
