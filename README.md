This project explores health indicators from the BRFSS 2015 dataset to build predictive models for diabetes.  


Requirements
- Python 3.8+


BFRSS 2015 sources:,

[data set source](https://www.cdc.gov/brfss/annual_data/annual_2015.html),


[code book](https://www.cdc.gov/brfss/annual_data/2015/pdf/codebook15_llcp.pdf)


a graph explaining the overlapping nature of a patient being plus-size and the tendency to get diabeties
<img width="764" height="490" alt="image" src="https://github.com/user-attachments/assets/1933a76a-8c89-4e4a-bdd2-0f17daaae04d" />



a heatmap showing how patients feel physically and mentally fell when asked on a scale 0 being OK and 4 being the worst
<img width="566" height="488" alt="image" src="https://github.com/user-attachments/assets/5cbc4a00-90b2-445f-b277-38d7d58d2c4e" />

as of 27th of septemper 

1. Data Collection

pulled the BRFSS Diabetes 2015 dataset (diabetes_012_health_indicators_BRFSS2015.csv).

Clear documentation of columns and meaning.


 2. Exploration & Preprocessing

Checked for missing values (both counts and percentages).

Looked at unique values per column to understand feature distributions.

Identified class imbalance in target (Diabetes_012 / Diabetes_binary).

Dropped irrelevant columns (AnyHealthcare, NoDocbcCost).

Handled low-variance features with VarianceThreshold.


3. Advanced Data Analysis

Engineered new features:

ComorbidityScore (aggregating comorbidities).

GeneralHealthScore (combined mental, physical, and general health).

DietQuality (fruits + veggies).

Converted ordinal/numerical features into bins:

BMI_Category (underweight, normal, overweight, obese).

Binned MentHlth and PhysHlth into severity levels.

Categorical encoding:

One-hot encoding (Sex, BMI/age/education/income categories).


4. Visualization

Plotted class imbalance distributions.

Correlation heatmaps to see feature relationships.

Boxplots, bar plots, and crosstabs (e.g., Mental vs Physical Health).
