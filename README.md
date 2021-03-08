# Who is looking for a new job?

A training institute which conducts training for analytics/ data science wants to expand their business to manpower recruitment, data science only, as well. A large number of candidates signup for their training. The company wants to connect these enrollees with their clients who are looking to hire employees working in the same domain. Before that, it is important to know which of these candidates are really looking for a new employment. This helps to reduce the cost and time as well as the quality of training or planning the courses and categorization of candidates.


## Dataset 
Information related to demographics, education, experience and features related to training as well are in hands. The dataset, which is devided into train and test sets, can be found here [kaggle](https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists?select=aug_train.csv).


## Task 
The goal of this task is to build model(s) that use the given features to predict the probability of a candidate looking for a new job or will work for the company. In particular, we have a binary classification problem; 1: looking for a job, 0: not looking for a job.


## Preprocessing 

There are in total 33.380 rows, i.e. enrollees which participated in the training, and 14 features. The dataset is imbalanced and 10 features are categorical, some with high cardinality.

<br />
| Features        | dtypes      | unique values| isnull sum  | isnull % |
| --------------- |:-----------:| ------------:| -----------:|---------:|
|enrollee_id |	int64	|19158	|0	|0.00|
|city|	object|	123|	0|	0.00|
|city_development_index	|float64|	93|	0|	0.00|
|gender	|object|	4	|4508	|23|.53|
|relevent_experience|	object|	2	|0|	0.00|
|enrolled_university|	object|	4|	386|	2.01|
|education_level|	object|	6	|460	|2.40|
|major_discipline|	object|	7	|2813	|14.68|
|experience|	object|	23|	65	|0.34|
|company_size	|object|	9	|5938	|30.99|
|company_type|	object|	7|	6140	|32.05|
|last_new_job|	object|	7|	423|	2.21|
|training_hours|	int64	|241	|0	|0.00|
|target	|float64	|2	|0	|0.00|

<br />

All the preproccessing steps can be found in the notebook **hr_analytics_ED.ipynb**. 

### Missing Values
If we would just drop all rows with missing values, we would end up loosing around 50% of the data. Thus, we apply the following strategy:
- All feautures with missing values less then 3%, in particular, *enrolled_university, education_level, experience, last_new_job*, will be filled with the most current value. 
- All other missing values will be labeled as *unknown*. 

### Categorical features
We use the *LabelEncoder()* from *sklearn* to impute for the categorical features.

## Baselinemodels 
As a baseline we will apply *logistregression* as well as a simple neural network with one hidden layer. 


