# KSI_DE-DA_Project
### An end to end data engineering and data analytics project

This project involves the use of the City Of Toronto's and Toronto Police KSI (Killed and Seriously Injured) dataset. This dataset contains various records and reports of automobile related collisions in the City of Toronto. More information regarding the dataset can be found here: https://open.toronto.ca/dataset/motor-vehicle-collisions-involving-killed-or-seriously-injured-persons/.

### Data Modelling

The dataset was first mapped into an ER model (instead of drawing keys and attributes protruding out the entity block like seen conventionally, I just included them in the entity block itself sort of like a uml table) and then converted into a relational model (both can be seen in data models folder). Some columns, not used in the dashboard, were not included. Please see the data_pipeline.ipynb file in the data engineering pipeline folder for information regarding the modelling process. 

![KSI Data Model (ER_v2)](https://github.com/user-attachments/assets/68fa3a28-7c65-4f1f-aa31-fe474323c5f0)
![KSI Data Model (Relational_new_v2)](https://github.com/user-attachments/assets/080e2cbb-5225-4077-b917-f5ba72665601)

### Architecture
This project involves the Google Cloud Platform (GCP) tech stack, leveraging Mage.ai (https://www.mage.ai/) for building an ETL pipeline (see mage files folder), BigQuery for data warehousing, Looker Studio for data visualization (see dashboard under dashboard builder folder) and Google Cloud Storage for managing data. 

![architecture](https://github.com/user-attachments/assets/0148e509-e3c6-4ce0-b9d0-f6218e7cce8a)

### Dashboard

Alternatively you can see the dashboard here: https://lookerstudio.google.com/reporting/fefbf9ae-1f97-4909-96a9-7fa2bbddb75d




