# Who is looking for a new job?

A company which is active in Big Data and Data Science wants to hire data scientists among people who successfully pass some courses which are conducted by the company. A large number of candidates signup for their training. To reduce the cost and time, as well as the quality of the training, the company wants to know which of these candidates really wants to work for them, or are most likely to look for a job, after completing the training. 


## Dataset 
Information related to demographics, education, experience and features related to training as well are in hands from candidates signup and enrollment. The dataset, which is devided into train and test sets, can be found here [kaggle](https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists?select=aug_train.csv).


## Task 
The goal of this task is to build model(s) that use the given features to predict the probability of a candidate looking for a new job or will work for the company. In particular, we have a binary classification problem; 1: looking for a job, 0: not looking for a job.

All the required packages are listed in **pyproject.toml**.


## Preprocessing 

All the preproccessing steps can be found in the notebook **hr_analytics_ED.ipynb**. 

There are in total 33.380 rows, i.e. enrollees which participated in the training, and 14 features. We have a total of 10 categorical features, some with high cardinality, and 4 numerical feautres. 

<br />

| Features        | dtypes      | unique values | isnull sum  | isnull % |
| --------------- |:-----------:| -------------:| -----------:|---------:|
|enrollee_id      |	int64	       |19158	|         0	|          0.00|
|city|	object|	123|	0 |	0.00|
|city_development_index	| float64 |	93|	0|	0.00|
|gender	|object|	4	| 4508	|23|.53|
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

The dataset is imbalanced, meaning we have an unequal class distribution:

<br />

| Class 0 (not looking for a job) | Class 1 (looking for a job) |
|:-------------------------------:|:---------------------------:|
| 75%                             | 25%                         | 

<br />


### Missing Values
If we would just drop all rows with missing values, we would end up loosing 47% of the data, that is, almost half. Since data is essential, we apply the following strategy:
- All feautures with missing values less then 3%, in particular, *enrolled_university, education_level, experience, last_new_job*, will be filled with the most frequent value. 
- All other missing values will be labeled as *unknown*. 

### Categorical features
We use the *LabelEncoder()* from *sklearn* to impute for the categorical features.


## Modelling
The modelling part can be found in the notebook **hr_analytic_modelling.ipynb**. 

We start by applying three common machine learning models; *LogisticRegression, RandomForestClassifier, SVC*. We then compute the accuracy score of the prediction made on a testset:

<br />

|ML model  |	score | 
|:--------:|:------:|
| SVC|	0.748086|	
|LogisticRegression	| 0.765658 |
|RandomForestClassifier	| 0.777140 | 

<br />

We can improve our scores by normalizing the data before it is fitted to the models:

<br />

|ML model  | score with normalized| 
|:--------:|:------:|
| SVC|	0.765484|	
|LogisticRegression	| 0.766875|
|RandomForestClassifier	| 0.778706| 

<br />

### SMOTE
The challenge of working with an imbalanced dataset is that most machine learning techniques will likely ignore, and in turn have poor performance on, the minority class, which is in our case the class 0 (enrollee not looking for a job). 

One approach to addressing imbalanced datasets is to oversample the minority class. The simplest approach involves duplicating examples in the minority class, although these examples don’t add any new information to the model. Instead, new examples can be synthesized from the existing examples. This is a type of data augmentation for the minority class and is referred to as the *Synthetic Minority Oversampling Technique*, or *SMOTE* for short.

We use the implementations provided by the [imbalanced-learn Python library](https://github.com/scikit-learn-contrib/imbalanced-learn). With the SMOTE technique we are able to improve the accuracy scores of *SVC* and *RandomForestClassifier*.

<br />

|ML model  |		score with normalized| score with normalized and SMOTE |
|:--------:|:-----------------------:|:-------------------------------:|
| SVC|	0.734732|	0.786766|
|LogisticRegression	| 0.766875| 0.734732|
|RandomForestClassifier	| 0.778706| 0.834280|

<br />

## Further Thoughts
Further thoughts on how to improve the accuracy score:
- Use a different encoder for the categorical features
- Apply a neural network to fit the data e.g. Autoencoder.
