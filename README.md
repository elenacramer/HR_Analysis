# Applying SMOTE to an Imbalanced Classification Problem

Classification is one of the most common machine learning problems. A common issue found in datasets that are used for classification is imbalance. Data imbalance usually reflects an unequal distribution of classes within a dataset. 

The challenge of working with an imbalanced dataset is that most machine learning techniques will likely ignore, and in turn have poor performance on, although typically it is performance on the minority class that is most important. 


One approach to addressing imbalanced datasets is to oversample the minority class. The simplest approach involves duplicating examples in the minority class, although these examples don’t add any new information to the model. Instead, new examples can be synthesized from the existing examples. This is a type of data augmentation for the minority class and is referred to as the *Synthetic Minority Oversampling Technique*, or *SMOTE* for short.

Here we will apply some common machine learning models to an imbalanced dataset both with and without the SMOTE technique and compare the results. 

All the required packages can be found in the file [pyproject.toml](https://github.com/elenacramer/HR_Analysis/blob/main/pyproject.toml).

## Dataset

A company which is active in Big Data and Data Science wants to hire data scientists among people who successfully pass some courses which are conducted by the company. A large number of candidates signup for their training. To reduce the cost and time, as well as the quality of the training, the company wants to know which of these candidates really wants to work for them, or are most likely to look for a job, after completing the training. 


Information related to demographics, education, experience and features related to training as well are in hands from candidates signup and enrollment. The dataset, which is devided into train and test sets, can be found here [Kaggle](https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists?select=aug_train.csv).

The goal is to predict the probability of a candidate looking for a new job or will work for the company. 


## Preprocessing 

All the preprocessing steps can be found in the notebook [hr_analytics_ED.ipynb](https://github.com/elenacramer/HR_Analysis/blob/main/hr_analytics_ED.ipynb). 

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

We have an unequal class distribution:

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
The modelling part can be found in the notebook [hr_analytic_modelling.ipynb](https://github.com/elenacramer/HR_Analysis/blob/main/hr_analytics_modelling.ipynb). 

We start by applying three common machine learning models; *LogisticRegression, RandomForestClassifier, SVC*. The following table shows the accuracy score of the prediction made on a testset:

<br />

|ML model  |	score | 
|:--------:|:------:|
| SVC|	0.75|	
|LogisticRegression	| 0.77 |
|RandomForestClassifier	| 0.78 | 

<br />

We can improve our scores for SVC and LogisticRegression by normalizing the data before it is fitted to the models:

<br />

|ML model  | score with normalized data| 
|:--------:|:------:|
| SVC|	0.77 |	
|LogisticRegression	| 0.77|
|RandomForestClassifier	| 0.78| 

<br />

The RandomForestClassifier, and in general all tree-based algorithms, is fairly insensitive to the scale of the features. The classifier consists of decision tree's and a decision tree is only splitting a node based on a single feature. The decision tree splits a node on a feature that increases the homogeneity of the node. This split on a feature is not influenced by other features. 

### SMOTE

We use the implementations provided by the [imbalanced-learn Python library](https://github.com/scikit-learn-contrib/imbalanced-learn). With the SMOTE technique we are able to improve the accuracy scores of *SVC* and *RandomForestClassifier*, but unfortunately not for the LogisticRegression:

<br />

|ML model  |		score with normalized data| score with normalized and SMOTE |
|:--------:|:-----------------------:|:-------------------------------:|
| SVC|	0.77 |	0.79 |
|LogisticRegression	| 0.77| 0.74|
|RandomForestClassifier	| 0.78 | 0.83 |

<br />


## Further Thoughts
Further thoughts on how to improve the accuracy score:
- Preprocessing:
  - Use a different encoder for the categorical features
  - Impute most frequent value for all the missing values instead of adding the label "unknown"
- Hyperparamter tuning
- Apply a neural network to fit the data e.g. Autoencoder
