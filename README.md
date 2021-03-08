# Who is looking for a new job?

A training institute which conducts training for analytics/ data science wants to expand their business to manpower recruitment, data science only, as well. A large number of candidates signup for their training. The company wants to connect these enrollees with their clients who are looking to hire employees working in the same domain. Before that, it is important to know which of these candidates are really looking for a new employment. This helps to reduce the cost and time as well as the quality of training or planning the courses and categorization of candidates.


<br />


## Dataset 
Information related to demographics, education, experience and features related to training as well are in hands. The dataset, which is devided into train and test sets, can be found here [kaggle](https://www.kaggle.com/aswathrao/hr-analysis).


<br />


## Task 
The goal of this task is to build model(s) that use the given features to predict the probability of a candidate looking for a new job or will work for the company. In particular, we have a binary classification problem; 1: looking for a job, 0: not looking for a job.

<br />

## Preprocessing 

There are in total 33.380 rows, i.e. enrollees which participated in the training, and 14 features. The dataset is imbalanced and 10 features are categorical, some with high cardinality.

<br />

| Features        | dtypes      | isnull sum  | isnull % |
| --------------- |:-----------:| -----------:| --------:|
|enrollee_id      | int64       |	0	      |0.00      |
|city             |	object	     | 0  |	0.00 |
|city_development_index	| float64 |	0	| 0.00 |
|gender	object |	7486 |	22.43 |
|relevent_experience	| object|	0	|0.00|
|enrolled_university|	object|	621	|1.86|
|education_level|	object|	852	|2.55|
|major_discipline|	object|	5231	|15.67|
|experience	| object	| 103	| 0.31|
|company_size |	object| 	8830 |	26.45|
|company_type|	object|	9369|	28.07|
|last_new_job	|object	|671|	2.01|
|training_hours|	int64|	0|	0.00|
|target|	int64	|0|	0.00|

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


