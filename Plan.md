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
**Basic Issues that must be resolved in this phase**
- **Data acquisition:** How do I find the data I need for modeling? 
- **Data integration:** How do I integrate data I find in multiple disparate data sources?
- **Data description:** What do the data look like?
- **Data assessment**: How clean is the data set?
### 1. Data acquisition
- Query-based data extracts from the database to flat files 
- High-level query languages for direct access to the database 
- Low-level connections for direct access to the database
#### Data access
  - Find and extract the right data for modeling.
#### Data integration
  - Combine data sets.
  - Data in relational databases must either be flattened (gathered together into one row or record), or the data map must be traversed to access the data in the databases directly through in-database access utilities, available in some analytic tools.
  - In addition to extraction, may field s of data must be transformed and new variables derived.
#### Initial data collection report
### 2. Data Description
#### Variables
#### Cases
#### Descriptive Statistics
- **Mean-average value**: shows the central tendency of a data set 
- **Standard deviation**: shows the distribution of data around the mean 
- **Minimum:** the lowest value 
- **Maximum:** the highest value 
- **Frequency tables:** show the frequency distribution of values in variables 
- **Histograms:** graphic technique to show frequency values in a variable
#### Data Description Report
### 3. Data Quality Assessment
- Missing values
- Outliers
- Any suspicious data (miscodes, training data, plain garbage).
- Data quality report
## Data Preparation
- **Data cleansing**: clean data
   - Validating codes against lists of acceptable values: many data mining tools offer some sort of expression language in the tool interface, which you can use to search and replace invalid codes in the data set.
   - Deleting particularly "dirty" records: not uncommonly, many variables have values (or blanks) that are inappropriate for the data set. You should delete these records. Their inclusion in the modeling data set will only confuse the model "signal" and decrease the predictive power of the model.
- **Data transportation**: express data variables
   - Numerical variables: many parametric statistical routines assume that the effects of each variable on the target are linear. This means that as X-variable increases by an amount A, then the target variable increases by some constant multiple of the amount A. This pattern of increase forms a geometric progression. However, when the multiple is not constant, the pattern increase forms an exponential pattern. If you want to use statistical parametric statistical modeling algorithms, you should transform any variables forming exponential (nonlinear) curves. Otherwise, estimation errors caused by the violation of the assumption of linearity could invalidate predictions made by the model.
   - Categorical variables: some categorial variables consisting of integers 1-9 will be assumed by the parametric statistical modeling algorithm to be continuous numbers. Such variables can be used safely, even though values between the integers (e.g. 1.56) are not defined in the data set. Other categorical variables may have textual categorials, rather than numeric values (e.g. entries consisting of red, blue, yellow, and green may require the definition of "dummy variables".
    - Dummy variables: a binary variable (coded as 1 or 0) to reflect the presence or absence of a particular categorical code in a given variable. 
   - Algorithms that depend on the calculations of covariance (e.g., regression) or that require other numerical operations (e.g., most neural nets) must operate on numbers. Dummy variables transform categorical (discrete) data into numerical data. Adding dummy variables to the analysis will help to create a better fit of the model, but you pay a price for doing so. Each raw variable that you represent by a group of dummies causes you to lose one degree of freedom in the analysis. The number of degrees of freedom represents the number of independent items of information available to estimate another item of information (the target variable). Therefore, the more tightly you fit your model (the more precise your model is), the more degrees of freedom you lose. Consequently, you have less information to work with, and you are left with less ability to apply the model successfully on other data sets, which may have a slightly different target pattern than the one you fit tightly with the model. This situation is called reducing the generality of the model. Generality is just as important (maybe even more so) than the accuracy of the model.
- **Data imputation**: handle missing values
  - A reasonable estimate of a suitable data value for the data missing in a variable is better than leaving it blank.
  - Assumption of Missing Completely at Random (MCAR): This assumption is satisfied when the probability of missing values in one variable is unrelated to the value of the variable itself or to values of any other variable. If this assumption is satisfied, then values of each variable can be considered to be a random sample of all values of this variable in the underlying population from which this data set was drawn. This assumption may be unreasonable when older people refuse to list their ages more often than younger people. This assumption may be reasonable when some variable is very expensive to measure and is measured for only a subset of the data set.
  - Assumption of Missing at Random (MAR): This assumption is satisfied when the probability of a value being missing in one variable is unrelated to the probability of missing data in another variable but may be related to the value of the variable itself. 
  - Techniques for imputing data (for missing data):
    - **Listwise (or casewise) deletion**: The entire record is deleted from the analysis. This technique is usually the default method used by many statistical and machine-learning algorithm.
      - Advantages:
        - Can be used for any kind of data mining analysis
        - No special statistical methods are needed to accomplish it
        - Safest methond when data is MCAR
        - Good for data with variables that are completely independent (the effect of each variable on the dependent variable is not affected by the effect of any other variable)
        - Usually, it is applicable to data sets suitable for linear regression and is even more apprpriate for use with logistic and Poisson regression.
      - Disadvantages:
        - You lose the nonmissing information in the record, and the total information content of your data set will be reduced.
        - If data is MAR, listwise deletion can produce biased estimates; if saslary level depends positively on education level (i.e. salary level rises as education level rises), then listwise deletion of cases with missing salary level data will bias the analysis toward lower education levels.
    - **Pairwise deletion**: This means that all cases wtih values for avariable will be used to calculate the covariance of that variable.
      - Advantages:
        - Linear regression can be estimated from only sample means and covariance matrix (listing covariances for each variable). 
        - Generates internally consistent matrics.
        - Only works with MCAR (MAR can lead to significant bias in the estimators).
    - **Reasonable value imputation**: Imputation of missing values with the mean of the nonmissing cases is referred to often as "mean substitution". If you can safely apply some decision rule to supply a specific value to the missing value, it may be closer to the true value than even the mean substitution would be.
    - **Maximum Likelihood Imputation**: This technique assumes that the predictor variables are independent. It uses a function that describes the probability density map (analogous to a topographic) to calculate the likelihood of a given missing value, using cases where the value is not missing. A second routine maximizes this likelihood, analogous to finding the highest point on the topographic map.
    - **Multiple Imputation**: Rather than to pick a value (e.g. mean) to fill blanks, a more robust approach is to let the data decide what value to use. This approach uses multiple variables to predict what values for missing data are most likely or probable.
      - Simple random imputation: This technique calculates a regression on all the nonmissing values in all of the variables to estimate the value that is missing. This approach tends to under-estimate standard error estimates. A better approach is to do this multiple times.
      - Multiple random imputation: In these techniques, a simple random imputation is repeated multiple times. This method is more realistic, because it treats regression parameters (e.g. means) as sample values within a data distribution. An elaboration of this approach is to perform multiple random imputation m-times with different data samples. The global mean imputed value is calculated across multiple samples and multiple imputations. 
  - Guidelines for choosing the best imputation technique to use.  
    1. If you have a lot of cases, delete records with missing values. 
    2. If you are using linear regression as a modeling algorithm, have a lot of data, have only a few missing values, and use listwise deletion. 
    3. If you are using SAS, use PROC MI. 
    4. If you have any insight as to what the value ought to be, fill missing values with reasonable values. 
    5. Otherwise, use mean imputation. 
    6. If the variable is very important, consider training a model to impute the missing values.
- **Data weighting and balancing**: are all cases treated the same?
- **Data filtering**: do something about outliers and other unwanted data
  - Eliminating rows (cases) in order to remove unnecessary information. This is done to clarify the "signal" of the variables to be modeled. Removing unnecessary information reduces the "noise" below the level of the analysis. Anagolously, a customer attrition signal in a corporate database is an expression of a customer retention domain in a company.
  - **Removal of Outliers**: The simplest way to handle outliers is to remove the rows that contain them. Sometimes, you want to keep the outliers (abnormal values). In fact, some outliers are of primary interest to the modeling of credit risk, fraud, and other rare events like network intrusions. For the models of "normal" responses, it might be a good idea to remove the extreme outliers by deletion of of the row or imputation of the value with a constant or the mean or median. If you leave the outliers in the data set, they will just inject noise, which will reduce the predictability of the model. But you might object that we should keep all values in the data, because we have to score values like this in our production operations of the model. You can afford to be wrong in your predictions 5% of the time, for example, for the sake of being very predictive on the other 95% of the data.
  - **Outlier detection algorithms**:
    - Those based on critical distance measures
    - Those based on density measures
    - Those based on projection characteristics
    - Those based on data distribtuion characteristics
  - **Time-Series Filtering**
    - Low-pass filter: A low-pass filter passes data below a specified highest level of acceptability. *e.g. the higher part of the fluctuations in the 3-month T-Bill rates might be eliminated from the data set.
    - High-pass filter: A high-pass filter does the opposite of a low-pass filter; it passes data above a specified lower level of acceptability.
    - Band-pass filter: The band-pass filter passes only data above a low value and below a high value. Although most data sets we prepare for modeling is not time series, signal processing techniques can be applied very effectively to data sets other than time-series data. We can use these techniques to analyze time-series data from billing systems and purchase records also. When you view a predictor variable in the context of its contribution in predicting a target variable, you can think of the contribution as a "signal" of the state or level of the target variable. Some variables might provide a stronger signal (be more predictive), and other variables may be less so. There will be a certain amount of "noise" (confusion in the target signal) in the values of the predictor variable. We can selectively remove some of this noise in ways very analogous to time-series signal filtering. 
      - A low-pass data can be implemented simply by eliminating cases with values below a certain threshold value. The effect of this operation will be to remove trivial inputs to the modeling algorithm. On the other hand, a high-pass filter can be used to remove above a threshold (outliers). One of the arts practiced in data mining is picking the right thresholds for these operations. To do this right, you must know the data domain very well. *e.g. data for telephone minutes for each month (MOU) show that average call durations are about 3 min in length. But, the curve tails off to the right for a long time. Retention data sets using MOU as a predictor variable for attrition (churn) should be filter with a high-pass filter to remove these outliers. The resulting model will be a much better predictor, just like a radio signal passed through a digital high-pass filter in a radio set will be much clearer to the hearer.*
- **Data abstraction**: handle temporal (time-series) data
  - Data preparation for data mining may include some very complex rearrangements of your data set. *E.g. you extract into an intermediate data set a year of call records by month for a group of customers. This data will have up to 12 records for each customer, which is really a time-series data set. Analyzing time-series data directly is complex, but there is an indirect way to do it by performing a reverse pivot on your intermediate data set. The records constitute a time series of up to 12 monthly billings ofr each customer. The first customer was active for the entire 12 months (12 records). But the second customer has only 9 records, because this person left the company. In many industries (including telecommunications), this loss of business is called* **attrition** *or* **churn**. *This data set could be analyzed by standard statistical or machine-learning time-series tools. Alternatively, you can create analytic records from this data set by doing a reverse pivot. This operation copies data from rows for a given customer and installs them in columns of the output record. A normal pivot does just the oppositve by copying column data to separate rows. This record is suitable for analysis by all statistical and machine-learning tools. Now that we have the time-dimensional data “flattened out” into an analytic record, we can reexpress the elements of this record in a manner that will show churn patterns in the data. But, in its present format, various customers could churn in any month. If we submit the current form of the analytic record to the modeling algorithm, there may not be enough “signal” to relate churn to MOU and other variables in a specific month. How can we rearrange our data to intensify the signal of the churn patterns? We can take a page out of the playbook for analyzing radio signals by performing an operation analogous to signal amplification. We do this with our data set by deriving as set of temporal abstractions, in which the values in each variable are related to the churn month. Instead of analyzing the relationship of churn (in whatever month it occurred) to specific monthly values (e.g., January MOU), we relate the churn month to the MOU value for the previous month, the month before the previous month, and so forth. The power of these temporal abstractions clarify the churn signal to our visual senses, and it will appear more clearly to the data mining algorithm also. These temporal abstractions are referred to commonly as “lag variables,” because the effect related to the target variable “lags” by a specified time period.*
  - Other data abstractions:
    - Qualitative abstraction: a numeric expression is mapped to a qualitative expression. *e.g. in an analysis of teenage customer demand, compared with that of others, customers with ages between 13 and 19 could be  abstracted as a value of 1 to a variable "teenager", while others are abstracted to a value of 0.*
- **Data reduction**: reduce the amount of data to use
- **Data sampling**: records
- **Dimensionality reduction**: variables
- **Data discretization**: values
- **Data derivation**: create new variables
## Modeling
### 1. Select Modeling Techniques
#### Choose modeling algorithms
How you prepare your data will depend to some degree on what modeling algorithm you choose (*e.g. if you choose a parametric statistical algorithm like multiple regression, you may have to transform variables to account for significant nonlinearity.*)
#### Choose modeling architecture
A simple analysis =  submitting data to the algorithm and evaluate the models created.   
To refine models and improve performance: 
- Some algorithms like neural nets permit you to adjust the algorithm architecture to improve performance (add hidden layers or increase the learning rate). 
- You can create a series of models, using different algorithms (ensembles)
- You can model on different samples of data and compare or combine results (bootstrap, jackknife resampling, and v-fold cross validation). 
- You can build some simple feedback processes in your models to iteratively improve your model (boosting). 
(*e.g. single analysis, ensamble etc.*)
#### Specify modeling assumptions
Choose an algorithm whos assumptions fit your data and your modeling goal.
(*e.g. among neural nets, radial basis function neural net handles outliers better than an ordinary neural net*).
### 2. Create an experimental design
### 3. Build a model
#### Set parameters
Study the default parameters of your modeling algorithm and the theory behind these settings. Create other models and see what happens.
#### Build various types of models
### 4. Assess the model
Some effecting techniques: using various tables and graphs (coincidence tables, lift charts, ROI curves, and normal probability charts).
### 5. Evaluate the model
Include them in a modeling report. This report will help to synthesize conclusions to form general insights about the modeling effort and to point the way to improving the results during the next modeling effort. 
## Deployment
1. Plan model deployment
  - Create deployment plan
2. Plan model monitoring and maintenance
  - Model monitoring plan
  - Model maintenance plan
3. Produce final report
  - Produce final written report
  - Produce final modeling presentation
4. Review project.
