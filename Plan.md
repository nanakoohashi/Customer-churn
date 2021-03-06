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
    - Qualitative abstraction: a numeric expression is mapped to a qualitative expression. *e.g. in an analysis of teenage customer demand, compared with that of others, customers with ages between 13 and 19 could be  abstracted as a value of 1 to a variable "teenager", while others are abstracted to a value of 0.*.
    - Generalization abstraction: an instance of an occurrence is mapped to its class. *e.g. in an analysis of Asian preferences, compared with non-Asian, listings of "Chinese", "Japanese", and "Korean" in the Race variable could be abstracted to 1 in the Asian variable, while others are abstracted to a value of 0.*
    - Definitional abstraction: in which one data element from one conceptual category is mapped its counterpart in another conceptual category. *e.g. When combining data sets from different sources for an analysis of customer demand among African-Americans, you might want to map "Caucasian" in a demographic data set and "White Anglo-Saxon Protestant" in a sociological data set to a separate variable of "Nonblack".
    - Temporal abstraction: see above.
- **Data reduction**: reduce the amount of data to use
  - Includes three general processes:
    1. Reduction of dimensionality (number of variables).
      - Now that we have our analytic record, we can proceed to weed out unnecessary variables using the following techniques:
        - **Correlation Coefficients**
          - One of the simplest ways to assess variable relationships is to calculate the simple correlation coefficients between variables. A correlation matrix shos pairwise correlation coefficients. These data have been used in many texts and papers as an example of predictor variables used to predict the target variable, crime rate.
          - From the correlation matrix we can learn two very useful things about our data set. First, we can see that the correlations of most of the variables with crime rate are relatively high and significant but that for Charles River proximity is relatively low and insignificant. This means that Charles River may not be a good variable to include in the model. The other thing we can learn is that none of the correlations of the predictor variables is greaer than 0.90. If a correlation between two variables exceeded 0.90 (a common rule-of-thumb threshold), their efficts would be too *collinear* to include in the model. Collinearity occurs when plots of two variables against the target lie on almost the same line. Too much collinearity among variables in a model (multicollinearity) will render the solution ill-behaved, which means that there is no unique optimum solution. Rather, there will be too much overlap in the effects of the collinear varaibles, making interpretation of the results problematic.
        - **CHAID (Chi-Square Automatic Interaction Detection)**
          - This algorithm is used occassionally as the final modeling algorithm, but it has a number of disadvantages that limit its effectiveness as a multivariate predictor. It is used more commonly for variable screening to reduce dimensionality. But even here, there is a problem of bias toward variables with more levels for splits, which can skew the interpretation of the relative importance of the predictors in explaing responses on the dependent variable. Despite the possible bias in the variable selection, it is used commonly as a variable screen method in several data mining tools (e.g. Statistica).
        - **Principal Components Analysis (PCA)**
          - Often used to identify some of the strong predictor variables in a data set.
          - Reveals relationships between variables in a data set by identifying and quantifying a group of principal components.
            - These principal components are composed of transformations of specific combinations of input variables that relate to a given output (or target variable).
            - Each principal component accounts for a decreasing amount of the variations in the raw data set. Consequently, the first few principal components express most of the underlying structure in the data set. Principal components have been used frequently in studies as a means to reduce the number of raw variables in the data set. When this is done, the original variables are replaced by the first several principal components. In such cases, the original features are simply replaced by the first few principal components. 
        - **Gini Index**
          - The Gini was developed by the Italian statistician Corrado Gini in 1912, for the purpose of rating countries by income distribution. The maximum Gini Index = 1 would mean that all the income belongs to one country. The minimum Gini Index = 0 would mean that the income is even distributed among all countries. This index measures the degree of unevenness in the spread of values in the range of a variable. The theory is that variables with a relatively large amount of unevenness in the frequency distribution of values in its range (a high Gini Index value) have a higher probability to serve as a predictor variable for another related variable.
        - **Graphical Methods**
          - You can look at correlation coefficients to gain some insight into relationships between numeric variables, but what about categorical variables?  Some data mining tools have specialized graphics for helping you to determine the strength of relationships between these categorical variables. *e.g. IBM Modeler provides the web node, which draws lines between categorical variables positioned on the periphery of a circle. The width connecting the lines represents the strength of the relationship between the two variables. The following web diagram shows a strong relationship between the preferences of “No” for Diet Pepsi and “No” for Diet 7 Up. There are no links between “Yes” for Diet Pepsi and Diet 7 Up. Therefore, you might expect that there might be a relatively strong relationship between the “No” preferences of these beverages. Other common techniques used for the reduction of dimensionality are the following:*
            - Multidimensional scaling 
            - Factor analysis 
            - Singular value decomposition 
            - Employing the “kernel trick” to map data into higher-dimensional spaces. This approach is used in support vector machines and other kernel learning machines, like KXEN. 
    2. Reduction of cases (records) - data sampling.
    3. Discretization of values.
- **Data sampling**: records
  - Data sampling serves four purposes:
    1. It can reduce the number of data cases submitted to the modeling algorithm.
      - In many cases, you can build a relatively predictive model on 10%–20% of the data cases. After that level, the addition of more cases has sharply diminishing returns. In some cases, like retail market basket analysis, you need all the cases (purchases) available. But usually, only a relatively small sample of data is necessary. This kind of sampling is called **simple random sampling**. The theory underlying this method is that each sample case selected has an equal chance of being selected as does any other case.
    2. It can help you select only those cases in which the reponse patterns are relatively homogenous.
      - If you want to model telephone calling behavior patterns, for example, you might judge that calling behaviors are distinctly different in urban and rural areas. If you divide your data set into urban and rural segments, it is called partitioning the database. It is a good idea to build separate models on each partition. When this partitioning is done, you should randomly select cases within each defined partition. Such a sampling is called **stratified random sampling**. The partitions are the “strata” that are sampled separately.
    3. It can help you balance the occurrence of rare events for analysis by machine-learning tools. 
      - Machine-learning tools like neural nets and decision trees are very sensitive to unbalanced data sets. An unbalanced data set is one in which one category of the target variable is relatively rare compared with the other ones. Balancing the data set involves sampling the rare categories more than average (oversampling) or sampling the common categories less often (undersampling).
    4. Simple random sampling can be used to divide the data set into three data sets for analysis: 
      a. Training set: These cases are randomly selected for use in training the model 
      b. Testing set: These cases are used to asses the predictability of the model, before refining the model or adding model enhancements. 
      c. Validation set: These cases are used to test the final performance of the model after all modeling is done. This sampling process is called partitioning. Most analytic tools have facilities for partitioning the data set. 
- **Dimensionality reduction**: variables
- **Data discretization**: values
  - Some machine-learning techniques can work with only categorical predictor variables, not continuous numeric variables. You can convert a continuous numeric variable into a series of categories by assigned subranges of the value range to a group of new variables. For example, a variable ranging from 1 to 100 could be discretized (converted into discrete values) by dividing the range in four subranges, 0–25, 26–50, 51–75, and 76–100. Another name for these subranges is “bins.” In the binning process, each value in the range of a variable is replaced by a bin number. Many data mining packages have binning facilities to create these subranges automatically. One of the attributes of the binning process is that it reduces “noise” in the data. To that extent, binning is a form of data smoothing. Credit scores are created using bins, in which bin boundaries are tuned and engineered to maximize the predictive power of the credit scoring model. The scorecard module in the Fair Isaac Model Builder tool is used to produce the FICO credit score. It uses a range engineering approach in the process of interactive binning to maximize the information content (IV) and weight of evidence (WOE) associated with a specific binning design. The IV provides a measure of the loss of information when bins are combined. The WOE relates the proportion of good credit scores with bad credit scores in each bin for that variable in the training data set. This approach to prediction engineers the data to maximize the predictability of a very simple linear programming modeling algorithm. Data preparation process:
    - Recoding data
    - Transforming data
    - Binning data
    - Smoothing data
    - Clustering data
- **Data derivation**: create new variables
  - **Assignment or Derivation of the Target Variable**: This operation defines the modeling goal in terms of available input variables. The modeling goal is to “hit” the target variable value with the prediction of the model. Often, the target variable can be selected from among the existing variables in the data set. For example, the target variable for a model of equipment failure could be the presence or absence of a failure date in the data record. In other cases, the target variable may be defined in a more complex manner. The target variable for customer attrition in a model created was defined as the month in which customer phone usage declined at least 70% over the previous two billing periods. This variable was derived by comparing the usage of all customers for each month in the time-series data set with the usage two billing periods in the past. The billing period of this cellular phone company was every 2 months, so the usage 4 months previous to each month was used as the value of comparison. Most often, the target variable must be derived following some heuristic (logical rule). The simplest version of an attrition target variable in that cellular phone company would have been to identify the month in which the service was discontinued. Insurance companies define attrition in that manner also.
  - **Derivation of New Predictor Variables**: New variables can be created from the combination of existing variables. For example, if you have access to latitude and longitude values for each case (e.g., a customer list), you might create a new variable, distance to store, by employing one of the simple equations for calculating distance on the surface of the Earth between two pairs of latitude-longitude coordinates. One common formula for calculating this distance is based on the law of cosines and expressed below in the form of an Excel cell formula: = ACOS(SIN(Lat1) * SIN(Lat2) + COS(Lat1) * COS(Lat2) * COS(Lon2-Lon1)) * 3934.31 
The value 3934.31 is the average radius of the Earth in miles, and output is the distance in miles between the two points. The latitude and longitude values must be expressed in radians, in order for the trigonometric functions to work properly. Other transformations might include the calculation of rates. For example, you could divide one variable (number of purchases) by another variable (time interval) to yield the purchase rate over time. The raw values of the number of purchases may show little relationship to attrition (customers leaving the company), while decline in purchase rates might be very predictive.
  - **Attribute-Oriented Induction of Generalization Variables**: This technique generalizes from a list of detailed categories in a variable to form a higher-level (more general) expression of a variable. For example, you might lack information about a customer's occupation. We could form the concept generalization, white-collar worker, based on specific levels in a number of other variables (e.g., yearly salary, homeowner, and number of cars). That induced variable might be very predictive of our target variable. You can also induce segmentation variables using this technique. For example, you might query the database of banking customer prospects against the customer database to find indirect relationships with these prospects, considering matching addresses, phone numbers, or secondary signer information on customer accounts. All matches could be coded as “Y” in a new variable, an indirect relationship variable, and all others are coded as “N.” All prospects with “Y” in the indirect relationship variable could be used as targets for a specific marketing campaign to sell to them direct banking services.
- **Data Conditioning**
  - All of the operations described above are performed on specific rows (cases) or columns (variables) in a data set. There are three common operations that are performed on the entire data set: (1) standardization, (2) balancing of data sets with rare target classes, and (3) segmentation.
  - **Standardization:** Some analytic algorithms assume that the ranges of all variables are nearly the same (e.g., regression algorithms). If one variable has a range that is significantly greater than the other variables, the parameter estimates will be biased toward the variable with the highest range. To conform the data set to that assumption, all ranges of variables are standardized. Standardization is the process of transforming a variable range with some mathematical heuristic, such that all variables have the same range. The most common heuristic used is the Z-transform 
    - Z=(X - *mean* )/Sd
    - where X is the variable value, mean is the average value for that variable, and Sd is the standard deviation of the variable.
- **Data Set Balancing:** Parametric statistical algorithms measure how far various derived metrics (e.g., means and standard deviations) are from critical values defined by the characteristics of the data distribution. For example, if a value in a data set is beyond 1.96 standard deviation units from the mean, it is beyond the value where it is probable that it could be a part of the other data set 95% of the time. This limit is called 95% confidence limit (or 95% CL). Parametric statistical algorithms like OLS learn things about the data by using all cases to calculate the metrics (e.g., mean and standard deviation) and compare all data values in relation to those metrics and standard tables of probability to decide if a relationship exists between two variables. Machine-learning (ML) algorithms learn in a very different way. Instead of going through all of the cases to calculate the summary metrics of the mean and the standard deviation, machine-learning algorithms learn case by case. For example, neural nets assign random weights to each variable on the first pass through the data. On subsequent passes through the data (sometimes 100 or more), the weights are adjusting in some process like back propagation, according to the effects of variables in each case. Without case weighting, variables in all cases have the same potential effect on adjusting the weights. Think of the weight applied to a rare event case as if it were a frequency applied for calculating a weighted mean. If the rare event is present in 5% of the cases, you could weigh the effect of the rare event cases by a factor = 0.95 and weight all other cases with 0.05 (the reciprocal of the frequency). Then, the backpropagation algorithm would be affected by the patterns in the rare cases equally as by the common cases. That is the best way for the neural net to distinguish the rare pattern in the data. This is just what is done by the Balance node in IBM SPSS Modeler. The Balance node puts out a report showing this weighting factor for each target state. The Balance node can be generated by the distribution node, which creates a frequency table on the target variable. This frequency factor becomes the weighting factor in the Balance node. If you want to use ML algorithms to model targets in unbalanced data sets, you balance the data set before modeling operations. 
  - There are a four common ways to balance a data set: 
    1. undersampling the common target class;
    2. oversampling the rare target class; 
    3. use weights associated with each variable, if the algorithm contains that feature; and 
    4. use prior probabilities, if the algorithm contains that feature.
- **Segmentation:** This is another example of the input of business knowledge in the analytic process. You might know (or strongly suspect) that the phone calling behavior of urban customers is quite different from that of rural customers. You might decide that you want to separate the rural from the urban customers and build separate models for each. In order to do that, you must divide the original data set into two pieces, one for rural customers and one for urban customers. This process is called data segmentation. 
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
# Feature Selection
After your analytic data set is prepared for modeling, you must select those variables (or features) to use as predictors. This process of feature selection is a very important strategy to follow in preparing data for data mining. A major problem in data mining in large data sets with many potential predictor variables is the **curse of dimensionality** (the increasing difficulty in training a model when more predictor variables are added to it). 
- Feature selection has the following immediate positive effects for the analysis: 
  - Speeds up processing of the algorithm 
  - Enhances data quality 
  - Increases the predictive power of the algorithm 
  - Makes the results more understandable 
- Therefore, one of the first jobs of the data miner is to develop a short list of variables. This abbreviated list will include (hopefully) only those variables that significantly increase the predictive power and the generalizing ability of the model.
## Types of Feature Selection
1. Feature Ranking Methods
  - Include the use of statistical metrics, like the correlation coefficient. A more complex feature ranking method is the Gini Index.
    - **Gini Index**
      - The Gini Index can be used to quantify the unevenness in variable distributions and income distributions among countries. The theory behind the Gini Index relies on the difference between a theoretical equality of some quantity and its actual value over the range of a related variable. This concept was introduced by Max O. Lorenz in 1905 to represent the unequal distribution of income among countries. 
    - **Bivariate Methods** 
      - Other bivariate methods like mutual information calculate the distance between the actual joint distribution of features X and Y and what the joint distribution would be if X and Y were independent. The joint distribution is the probability distribution of cases in which both events X and Y occurring together. 
    - **Multivariate Methods**
      - Stepwise Linear Regression
        - A slightly more sophisticated method is the one used in stepwise regression. This is a classical statistics method that calculates the F-value for the incremental inclusion of each variable in the regression. The F-value is equivalent to the square root of the Student’s t-value, expressing how different two data samples are, where one sample includes the variable and the other sample does not. The t-value is calculated by:
          - t = difference in sample means/standard deviation of differences
          - F = √t - value
        - The F-value is sensitive to the number of variables used to calculate the numerator of this ratio and to the number of variables used to calculate the denominator. Stepwise regression calculates the F-value both with and without using a particular variable and compares it with a critical F-value either to include the variable (forward stepwise selection) or to eliminate the variable from the regression (backward stepwise selection). In this way, the algorithm can select the set of variables that meets the F-value criterion. It is assumed that these variables account for a sufficient amount of the total variance in the target variable in order to predict it at a given level of confidence specified for the F-value (usually 95%). If your variables are numeric (or can be converted to numbers), you can use stepwise regression to select the variables you use for other data mining algorithms. But there is a “fly” in this ointment. Stepwise regression is a parametric procedure and is based on the same assumptions characterizing other classical statistical methods. Even so, stepwise regression can be used to give you one perspective on the short list of variables. You should use other methods and compare lists. Don't trust necessarily the list of variables included in the regression solution, because their inclusion assumes linear relationships of variables with the target variable, which in reality may be quite nonlinear in nature.
      - **Partial Least Squares Regression** 
        - A slightly more complex variant of multiple stepwise regression keeps track of the partial sums of squares in the regression calculation. These partial values can be related to the contribution of each variable to the regression model. Statistica provides an output report from partial least squares regression, which can give another perspective on which to base feature selection. In the example of this output report for an analysis of manufacturing failures. It is obvious that variables 1 and 3 (and marginally variable 2) provide significant contributions to the predictive power of the model (total R2 = 0.934). On the basis of this analysis, we might consider eliminating variables 4 through 6 from our variable short list.
      - **Sensitivity Analysis**
        - Some machine-learning algorithms (like neural nets) provide an output report that evaluates the final weights assigned to each variable to calculate how sensitive the solution is to the inclusion of that variable. These sensitivity values are analogous to the F-values calculated for the inclusion of each variable in stepwise regression. 
          - Less precise than linear stepwise regression, but the neural net set of variables may be much more generalizable, by virtue of their ability to capture non-linear relationships effectively.
    - Complex Methods 
      - A piecewise linear network uses a distance measure to assign incoming cases to an appropriate cluster. The clusters can be defined by any appropriate clustering method. A separate function called a basis function is defined for each cluster of cases. A pruning algorithm can be applied to eliminate the least important clusters, one at a time, leading to a more compact network. This approach can be viewed as a nonlinear from of stepwise linear regression.
      - Multiple Adaptive Regression Splines (MARS):
        - The MARS algorithm solves regression and classification problems with multiple outcomes (target variables). This approach can be viewed as a form of piecewise linear regression, which adapts a solution to local data regions of similar linear response. Each of the local regions is expressed by a different basis function. MARS algorithms can also be viewed as a form of regression trees, in which the “hard” splits into separate branches of the tree are replaced by the smooth basis functions.
2. Best Subset Selection
- This approach to feature selection evaluates a subset of features, which have significant effect on as a group for suitability. The most common subset selection approaches are wrapper-  based. Wrappers use a search algorithm to search through the space of possible features and evaluate each subset by running a model on the subset. Some wrapper methods perform this evaluation with different randomly selected subsets, using a cross validation method. Cross validation divides the data set into a number of subsets for each group of features and evaluates a model trained on all but one subset. The subset not used for the model is used to validate the model for that iteration. During the next iteration, a different random subset is used for validation. One way to use wrapper-based feature selection methods cheaply is to use RapidMiner, a GNU open-source data mining package. RapidMiner provides four feature selection methods:
  - Backward selection (feature selection), using multiple subsets 
  - Feature weighting using nearest neighbor 
  - Wrapper-based feature selection 
  - Automatic feature selection 
- The Feature Selection node in STATISTICA Data Miner (SDM) is very easy to use, especially in the “Data Miner Workspace” and also automatically behind the scenes without the user having to do anything in the “Data Miner Recipe” format. SDM has three formats for doing data mining: 
  1. Interactive module, where “Feature Selection” is available 
  2. Data Miner Workspace, where the user has the most control over “Feature Selection” 
  3. Data Miner Recipe, where “Feature Selection” is basically automatic
## Why Use Feature Selection? 
Considering the relatively little effect of feature selection on the German Credit data, you might wonder why we should do it at all. There are two primary reasons to use feature selection with machine-learning algorithms (particularly with tree algorithms): 
1. Decision tree models (like those trained by the C&RT algorithm) are very subject to overtraining. The algorithm designers try to minimize this effect by pruning tree branches and by error checking the prediction by using the trained model to predict  the testing data set. Overtrained decision trees may now work nearly as well with new data sets of the format, because of changes over time in the underlying relationships between the target and predictor variables. 
2. All prediction algorithms work better with fewer variables, because the complexity and dimensionality of the decision space is relatively smaller and the algorithm has to evaluate many fewer possibilities (candidate trees in the case of C&RT). Without feature selection, it is true that inclusion of more variables in the model may increase the probability of gaining more important predictors but it also increase the complexity of the mathematical solution exponentially. This is referred to as the curse of dimensionality. Feature selection with a competent algorithm can minimize the effects of dimensionality that plagues all predictive algorithms. 
3. Some data sets have far too many variables to process efficiently with machine-learning or statistical analysis algorithms. For example, the KDD Cup 2001 competition data set had 139,000 variables and only about 2000 cases! It is crucial in cases like this to use feature selection to reduce the variable count. 
- There are two other ways to use feature selection facilities in SDM: (1) the Interactive Menus Interface and (2) the DMRecipes automated modeling interface.
# Accessory Tools for Doing Data Mining
The following tools can help the data miner:
- Data access tools: SQL and other database query languages 
- Data integration tools: extract-transform-load (ETL) tools to access, modify, and load data from different structures and formats into a common output format (e.g., database and flat file) 
- Data exploration tools: basic descriptive statistics, particularly frequency tables; slicing, dicing, and drill downs 
- Model management tools: data mining workspace libraries, templates, and projects 
- Modeling analysis tools: feature selection; model evaluation tools. (Note: This topic will be expanded in Chapter 11.) 
- Miscellaneous tools: in-place data processing (IDP) tools, rapid deployment tools, and model monitoring tools Being able to use these tools properly can be very helpful in the identification of significant variables, facilitating rapid decision-making necessary to compete successfully in the global marketplace.
## Basic Descriptive Statistics 
### Measures of Location 
- Mean: the average for all observations in the range of a variable 
- Median: the middle observation in a sorted list of values in the range for a given variable 
- Mode: the most frequently occurring value
### Measures of Dispersion 
- Variance: a measure of the variability of squared values around the mean 
- Standard deviation: the square root of the variance 
- If the data are tightly clustered around the mean, the variance and standard deviation are relatively low. If the data are widely scattered around the mean, the variance and standard deviation are relatively high.
### Range 
- Maximum: the highest value in the range of a variable 
- Minimum: the lowest value in the range of a variable 
- Together with the mean and standard deviation, the maximum and minimum values can be useful in identifying outliers (values so much higher or so much lower than the vast majority of values that they appear to be the result of another process). Outliers may be mistaken readings, garbage data, or they may be very rare but valid measurements. Sometimes apparent outliers are the very values that may contain a disproportionately large amount of the signal of the target variable. The data miner is justified in deleting mistaken readings and garbage data. Under certain conditions, you might be justified in deleting even the very rare by valid measurements, because doing so will reduce the variance in the range of a variable, making it a stronger predictor of the target. In any event, the data miner should decide how to handle outliers in the context of the problem and his or her domain knowledge.
### Measures of Position 
- Quantiles: a portion of the total number of observations. Quantiles are usually names according to the number of portions into which the range is divided. 
- Quartiles: 4 portions. 
- Quintiles: 5 portions. 
- Deciles: 10 portions. 
- Percentiles: 100 portions. There are many types of percentiles, including the following: 
- The PTH percentile: value where at least p percent of the items are less than or equal to this value and (100 − p)% of the items are greater than or equal to this value 
- Median percentile: 50th percentile
- Q1: first quartile = 25th percentile 
- Q3: third quartile = 75th percentile
### Measures of Shape 
- Skewness: the degree to which the distribution of data for a variable is largely to one side of the mean 
- Kurtosis: the degree to which distribution of the data for a variable is closely arranged around the mean
### Robust Measures of Location 
- Trimmed mean is calculated by removing a percentage of values from both ends of the data set. A trimmed mean, therefore, is the arithmetic average after x-percentage of values has been removed from the highest and lowest ends of the data set.  
- Winsorized mean is the mean computed after the x-percentage highest and lowest values are replaced by the next adjacent value in the distribution. For example, consider an ordered data set with 100 observations, x1, x2, x3,…, x98, x99, and x100. If you request a winsorized mean with 5%, then the bottom 5% of values (x1, x2, x3, x4, and x5) will be replaced with the next adjacent value in the distribution (x6). Likewise, the top 5% (x96, x97, x98, x99, and x100) will be replaced with x95.
### Frequency Tables 
In practically every research project, an initial examination of the data set usually includes frequency tables. In survey research, for example, frequency tables can show the number of males and females who participated in the survey, the number of respondents from particular ethnic and racial backgrounds, and so on. Responses on some labeled attitude measurement scales (e.g., interest in watching football) can also be nicely summarized via the frequency table. In medical research, you may tabulate the number of patients displaying specific symptoms; in industrial research, you may tabulate the frequency of different causes leading to catastrophic failure of products during stress tests (e.g., which parts are actually responsible for the complete malfunction of television sets under extreme temperatures). Customarily, if a data set includes any categorical data, then one of the first steps in the data analysis is to compute a frequency table for those categorical variables. Frequency or one-way tables represent the simplest method for analyzing categorical (nominal) data. They are used often to review how different categories of values are distributed in the sample. For example, in a survey of spectator interest in different sports, we could summarize the respondents' interest in watching football in a frequency table
# Basic Algorithms for Data Mining
## Basic Data Mining Algorithms 
- **Association rules**
  - The goal of association rules is to detect relationships or associations between specific values of categorical variables in large data sets. This technique allows analysts and researchers to uncover hidden patterns in large data sets. The classic example of an early association analysis found that beer tended to be sold with diapers, pointing to the cooccurrence of watching Monday Night Football and caring for family concerns at the same time. Variants like the a priori algorithm use predefined threshold values for detection of associations.
  - How association rules work. Assuming you have a record of each customer transaction at a large book store, you can perform an association analysis to determine which other book purchases are associated with the purchase of a given book. With this information in hand at the time of purchase, you could recommend to the customer a list of other books the customer may wish to purchase. Such an application of association analysis is called a “recommender engine.” 
  - Association algorithms can be used to analyze simple categorical variables, dichotomous variables, and/or multiple target variables. The algorithm will determine association rules without requiring the user to specify the number of distinct categories present in the data or any prior knowledge regarding the maximum factorial degree or complexity of the important associations (except in the a priori variant). A form of cross tabulation table can be constructed without the need to specify the number of variables or categories. Hence, this technique is especially well suited for the analysis of huge data sets. 
- **Automated neural networks**
  - Neural networks used for computation were based on early understandings of the structure and function of the human brain. 
  - Neuron cells receive electric impulses from neighboring cells and accumulate them until a threshold value is exceeded. Then, they “fire” an impulse to an adjacent cell across a gap called a “synapse.” The capacity of the cell to store electric impulses and the threshold is controlled by biochemical processes, which change over time. The distance of the synapse between two neurons is analogous to a resistor in an electric circuit. This gap between neurons is modifiable in the human mind, and any change in it is under the control of the autonomic nervous system. The accumulation potential of a neuron, the activation threshold, and the distance between neurons in the human brain is trainable. This is the primary means by which we “learn” to think or activate our bodies.
  - Artificial neurons in networks incorporate these three factors and vary them numerically, rather than biochemically. The aggregation process accepts data inputs by summing them (usually). The activation process is represented by some mathematical function, usually a linear or logistic function. Linear activation functions work best for numerical estimation problems (i.e., regression), and the logistic activation function works best for classification problems.
  - Artificial neurons are connected together into an architecture or processing structure. This architecture forms a network, in which each input variable (called an input node) is connected to one or more output nodes. This network is called an artificial neural network (ANN). In a simple two-layer ANN, inputs are connected to a summation aggregation function and a stepped activation function, which are in turn connected to an output node. This architecture was not very good for expressing any nonlinear relationship between the target variable (the output) and the predictor variables (Xi). A later innovation replaced the stepped function with an exponential function like the logistic function. The processing and output of such a neural network is functionally equivalent to a logistic regression with a binary output. This configuration of a neural net is a better classifier than the ANN with a stepped activation function. It has the ability to handle nonlinear relationships between the output and the combined effects of the input variables, by virtue of the logistic function.
  - A major innovation in the architecture design was the addition of a third layer, the “hidden” layer. This hidden layer permitted the expression of a large degree of the different nonlinear relationship between the inputs and the output (target) variable. Weights (Wij) are assigned to each connection between the input nodes and middle layer nodes and between the middle layer nodes and the output node(s). These weights are analogous to the gap distance between two neural members of a neural network. Herein lies the great value of a three-layer neural net for solving data mining problems. The nodes in the middle layer provide the capacity to model nonlinear relationships between the input nodes and the hidden layer nodes, and between them to the output node (the decision). The greater the number of nodes in the middle layer, the greater the capacity there is for the neural net to recognize nonlinear patterns in the data set. But, as the number of nodes increases in the middle layer, the training time increases exponentially, and it increases the probability of overtraining the model. An overtrained model may fit the training set very well, but not perform very well on another data set. Unfortunately, there are no great rules of thumb to define the number of middle layer nodes to use. The only guideline is to use more nodes when you have a lot of training cases and use fewer nodes with fewer cases. If your classification problem is complex, use more nodes in the middle layer; if it is simple, use fewer nodes. Most ANN implementations, however, do not permit the specification of the number of hidden layers. The “feed-forward” label means that data flow is from input forward to output. Some modern ANNs permit flow of information from one row backward to modify the processing of a subsequent row and allow the algorithm to adapt as subsequent rows of data are input. This capability permits the processing of time-series data, in which one value in a time series is dependent to some degree upon subsequent values (called serial autocorrelation). The ANN architecture can be constructed to contain only one output node and be configured to function as a regression (for numerical outputs) or binary classification (yes/no or 1/0). Alternatively, the net architecture can be constructed to contain multiple output nodes for estimation, classification, or even function as a clustering algorithm. The learning process of the human neuron is reflected (crudely) by performing one of a number of weight adjustment processes, the most common of which is called back propagation. The back-propagation operation adjusts weights of misclassified cases based on the magnitude of the prediction error. This is an adaptive process, which iteratively retrains the model and improves its fit and predictive power.
 - **Advantages**
  - Are general classifiers—they can handle problems with very many parameters, and they are able to classify objects well even when the distribution of objects in the Ndimensional parameter space is very complex. 
  - Can handle a large amount of nonlinearity in the predictor variables. 
  - Can be used for numerical prediction problems (like regression). 
  - Require no underlying assumption about the distribution of data. 
  - Are very good at finding nonlinear relationships. The hidden layer(s) of the neural net architecture provides this ability to model highly nonlinear functions efficiently. 
 - **Disadvantages** 
  - They may be relatively slow, especially in the training phase but also in the application phase. 
  - It is difficult to determine how the net is making its decision or to identify the important predictors in the solution. It is for these reasons that neural nets have the reputation of being a “black box.” 
  - No hypotheses are tested, and no P-values are available in the output for comparing variables.
 - **Modeling a manually configured ANN**
  - Learning Rate
  - Learning Rate Decay
  - Momentum
  - Number of Nodes in the Middle Layer
  - Number of Middle Layers to Add
 - **Additional Types of Neural Networks**
  - Linear networks—two layers (input and output layer), does not handle complexities well and can be considered as a “baseline model”     - Bayesian networks 
  - Probabilistic network (PNN)—consisting of 3–4 layers 
  - Generalized regression (GRNN)—trains quickly but executes slowly 
  - Deep learning—ANNs with more than one hidden layer, may be recurrent in design
  - Kohonen neural nets (Kohonen, 1982)—used for classification. This type of neural network is sometimes called a “self-organizing” neural net. The operation of it is to iteratively classify inputs, until the combined difference between classes is maximized. This algorithm can be used as a simple way to cluster data, if the number of cases or categories is not particularly large. For data sets with a large number of categories, it can take a very long time to train the network. 
  - **Radial Basis Function (RBF)**
    - Networks RBFs are similar to MLPs with three layers (input, middle or “hidden” layer, and output). Also like MLPs, RBFs can model any nonlinear function easily. The major difference between the two networks is that an RBF does not input raw input data but rather it passes a distance measure from the inputs to the hidden layer. This distance is measured from some center value in the range of the variable (sometimes the mean) to a given input value in terms of a Gaussian function These distances are transformed into similarities that become the data features worked with in a succeeding regression step. This nonlinear function can permit the mapping operation to capture many nonlinear patterns in the input data. The processing of RBFs (like any neural network) is iterative. The weights associated with the hidden nodes are adjusted following some strategy (like back propagation). If a large enough RBF is run through enough iterations, it can approximate almost any function almost perfectly; that is, it is theoretically a universal approximator. The problem with RBF processing (like with the MLP) is the tendency to overtrain the model.
   - **Advantages of RBFs**
    - RBFs can model any nonlinear function using a single hidden layer, which removes some design decisions about numbers of layers to use for the networks like the MLP. The simple linear transformation in the output layer can be optimized fully using traditional linear modeling techniques, which are fast and do not suffer from problems such as local minima which plague MLP training techniques. RBF networks can therefore be trained extremely quickly (i.e., orders of magnitude faster than MLPs).
   - **Disadvantages of RBFs**
    - On the other hand, before linear optimization can be applied to the output layer of an RBF network, the number of radial units must be decided, and their centers and deviations must be set. Although faster than MLP training, the algorithms to do this are equally prone to discovering suboptimal combinations.
 - **Automated Neural Nets**
  - Several data mining tools offer neural nets that have “smart” search algorithms to choose the appropriate starting points for their parameters. But, the biggest benefit of these algorithms is that they search over the decision surface with different initial learning rates (which also decay between iterations), different momentums, and different number of nodes in the middle layer. Usually, you have to choose the number of middle layers to use before the algorithm takes over. 
 - **Generalized Additive Models (GAM)**
  - As theory of general linear models (GLMs) developed in the 1980s, the need for an increasing number of predictor variables was recognized as a key issue. The problem with increasing the number of predictor variables is that the variance increases also. The higher the variance, the harder it is for a prediction algorithm to perform well (perform acceptably on new data). This is one aspect of the “curse of dimensionality.” To bypass this problem, Stone (1986) proposed the modification of the GLM by replacing the definition of each predictor variable with an additive approximation term. This approximation is performed with a linear univariate smoothing function. This approach avoided the curse of dimensionality by performing a simple fitting of each predictor variable to the dependent variable. The new approach also expressed the definition of each predictor variable such that it was possible to relate how the variable affected the dependent variable. Remember, in the standard multiple linear regression (MLR) equation, the estimated coefficients represent effects of differing scale and differing relationships to the dependent variable. Consequently, you can't analyze the MLR coefficients directly to determine relationships. But with the enhancement by Stone, one can see these relationships directly. Still, the cost of that enhancement was a decrease in generalization (ability to perform acceptably on new data). 
  - Typical outputs of GAMs include the following: 
    - Iteration history of model fitting 
    - Summary statistics, including R2 
    - Residual tables and plots 
    - Scatterplots of observed versus predicted values 
    - Normal probability plots
 - **Classification and Regression Trees (CART)**
  - Key elements defining a decision tree algorithm are the following: 
    - Rules at a “node” for splitting the data according to its value on one variable ◦ These splits are made at a “cut point,” determined by heuristics 
    - A “stopping” rule for deciding when a subtree is complete 
    - Assigning each terminal “leaf” node to a class outcome (prediction)
  - Trees recursively partition the data, creating at each step more homogenous groups. The resulting “rules” are the paths it takes to get from the “root” node to each “leaf” node. 
- **Recursive Partitioning** 
  - Once a best split if found, CART repeats the search process for each node below (“child” nodes), until further splitting is either stopped by a criterion or is impossible. Common stopping conditions include the following: 
    - Minimum number of cases 
    - A certain fraction of the total number of cases is in the node 
    - A maximum number of levels of splitting has been achieved 
    - The maximum number of nodes has been reached
  - Conditions under which further splitting is impossible include when 
    - only one case is left in a node, 
    - all cases are duplicates of each other, 
    - the node is pure (all target values agree).
 - **Pruning Trees**
  - Rather than focusing on when to stop pruning, CART trees are grown larger than they need to be and then pruned back to find the best tree. CART determines the best tree by using the testing data set or by the process of V-fold cross validation. The testing validation is performed by scoring the tree with the data set not used for training the model. Cross validation is a form of resampling, which draws a number of samples from the entire distribution and trains models on all samples. The V-fold cross validation is performed by the following: 
    1. Partitioning the entire data set in to a number (V) of parts (folds) 
    2. Training V models on different combinations of V-1 folds, with the error estimated each time using the Vth fold 
    3. Using the mean (and sigma) of the V error measurements to estimate tree accuracy on new data 
    4. Choose the design parameters (e.g., complexity penalty) that minimize the error in step 3 
    5. Refit the tree, using all the data and using the parameters of step 4
  - General Comments About CART for Statisticans 
    1. CART is nonparametric and does not require specification of a data distribution. 
    2. The final modeling variables are not selected beforehand, but automatically by the algorithm.
    3. There is no need to transform data to be consistent with a given mathematical function. Monotonic transformations will have no effect. 
    4. Very complex interaction patterns can be analyzed. 
    5. CART is not significantly affected outliers in the input space. 
    6. CART is affected but only locally by outliers in the output variable. 
    7. CART can accept any combination of categorical and continuous variables.
    8. CART can adjust for samples stratified on a categorical dependent variable.
    9. CART can process cases with missing values; the cases are not deleted.
  - Advantages of CART Over Other Decision Trees 
    1. You can relax the stopping rules to “overgrow” decision trees and then prune back the tree to the optimal size. This approach minimizes the probability that important structure in the data set will overlooked by stopping too soon. 
    2. CART incorporates both testing with a test data set and cross validation to assess the goodness of fit more accurately. 
    3. CART can use the same variables more than once in different parts of the tree. This capability can uncover complex interdependencies between sets of variables.
    4. CART can be used in conjunction with other prediction methods to select the input set of variables. 
    5. CART can be incorporated into hybrid models, where CART feeds inputs to a neural network model (which itself cannot select variables). 
  - Uses of CART 
    1. CART is simple! 
    2. Data preparation. Classical statistical models require that the analyst has a clear understanding of the nature of the function inherent in the data to be modeled. CART requires very little inputs for the beginning data miner.
    3. Variable selection. Cart can be used to create the short list of predictor variables to submit to the modeling algorithm. There is no guarantee that the variables most useful for a tree will also prove most useful for a neural network or other function, but in practice, this is a useful technique. 
    4. The use of predictors multiple times in the tree helps to detect complex interactions in the data. 
    5. CART can handle missing values by identifying surrogate (alternate) splitting rules. During training, after the best split is found for a node, new splits using other variables are scored according to their similarity in distributing the data to the left and right child nodes. The best five or so are then stored as backup or surrogate questions to ask should the main variable not be available.
- **General CHAID Models**
  - CHAID is an acronym for chi-squared automatic interaction detector. CHAID differs from CART by allowing multiple splits on a variable. For classification problems, it relies on the chi-squared test to determine the best split at each step. For regression problems (with a continuous target variable), it uses the F-test. Key elements of the CHAID process are as follows: 
    1. Preparing the predictor variables—Continuous variables are “binned” to create a set of categories, where each category is a subrange along the entire range of the variable. This binning operation permits CHAID to accept both categorical and continuous inputs, although it internally only works with categorical variables. 
    2. Merging categories—The categories of each variable are analyzed to determine which ones can be merged safely to reduce the number of categories. 
    3. Selecting the best split—The algorithm searches for the split point with the smallest adjusted P-value (probability value that can be related to significance). 
  - Advantages of CHAID 
    1. It is fast! 
    2. CHAID builds “wider” decision trees, because it is not constrained (like CART) to make binary splits, making it very popular in market research. 
    3. CHAID may yield many terminal nodes connected to a single branch, which can be conveniently summarized in a simple two-way contingency table, with multiple categories for each variable. 
   - Disadvantages of CHAID 
    1. Since multiple splits fragment the variable's range into smaller subranges, the algorithm requires larger quantities of data to get dependable results. 
    2. The CHAID tree may be unrealistically short and uninteresting, because the multiple splits are hard to relate to real business conditions. 
    3. Variables of the real data-type variables (continuous numbers with decimals) are forced into categorical bins before analysis, which may not be helpful, particularly if the order in the values should be preserved. The binned categories are inherently unordered; therefore, it is possible for CHAID to group “low” and “high” versus “middle,” which may not be desired.
- Generalized EM and k-means cluster analysis advanced data mining algorithms —interactive trees (CART or C&RT and CHAID) 
- Boosted tree classifiers and regression 
- MARSplines (multivariate adaptive regression splines) 
- Random forests for regression and classification 
- Machine learning (Bayesian, support vectors, and nearest neighbor) 
- Sequence, association, and link analysis 
- Independent components analysis
## Special-Purpose Algorithms 
- Text and document mining and Web crawling: file, document, and Web (URL) retrieval 
- Text mining and document retrieval quality control data mining and root cause analysis: quality control charts 
- Quality control charts for variable lists 
- Predictive quality control 
- Root cause analysis 
- Response optimization for data mining models
# Model Evaluation and Enhancement
- Cross validation resampling method 
- Bootstrap 
- Jackknife
## TYPES OF ERRORS IN ANALYTICAL MODELS
Errors can be classified into two general types: random error and systematic error. Random error is attributable to random variation in the target value “signal” caused by factors that cannot be accounted for by the predictor variables of even a perfect model. But no model is perfect. All modeling algorithms have strengths and weaknesses, which cause errors in the predicted values. Systematic error is caused by weaknesses in the random sampling and processing operations of the modeling algorithm or errors in model specification. We will consider evaluation methods based on the following: 
- Analyses of the predictive power of the model, apart from error 
- Analyses of random error in the model 
- Analyses of systematic error in the model
