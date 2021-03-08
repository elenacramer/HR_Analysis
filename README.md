# Who is looking for a new job?

A training institute which conducts training for analytics/ data science wants to expand their business to manpower recruitment, data science only, as well. A large number of candidates signup for their training. The company wants to connect these enrollees with their clients who are looking to hire employees working in the same domain. Before that, it is important to know which of these candidates are really looking for a new employment. This helps to reduce the cost and time as well as the quality of training or planning the courses and categorization of candidates.

<br />

## Dataset 
Information related to demographics, education, experience and features related to training as well are in hands. The dataset, which is devided into train and test sets, can be found here [kaggle](https://www.kaggle.com/aswathrao/hr-analysis).

<br />

There are in total 33.380 rows, i.e. enrollees which participated in the training, and 14 features. The dataset is imbalanced and 10 features are categorical, some with high cardinality. Here is an overview of the dataset:
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



 while only 2.425, or around 7%, of them where actually looking for a new job. 

<br />

*Notation:* the feature **target** describes if someone is looking for a new job or not; 0 – not looking, 1 – looking. 

<br />

## Do experienced people tend to look for a new job?

<br />

One might assume that people with no relevant experience participate in the training with a job change in mind. Why else participate, right? 

![Relevant_Experience](relevant_experience.png)

Most enrollee have relevant experience in the field. Among those with relevant experience, 7% are looking for a new job. While among those with no relevant experience, 10% are looking for a new job. Hence, we see that the difference is not as big as one might assume! 

<br />

What about the amount of experience? Are participians with a short term work experience more likely to look for a new job? 

![experience_relevant_experience](experience_relevant_experience.png)

<br />

## Does the educational background matter? 


<br />

## Do experienced people tend to look for a new job?

