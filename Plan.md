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
- **Data imputation**: handle missing values
- **Data weighting and balancing**: are all cases treated the same?
- **Data filtering**: do something about outliers and other unwanted data
- **Data abstraction**: handle temporal (time-series) data
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
