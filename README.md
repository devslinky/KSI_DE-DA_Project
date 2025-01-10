# KSI_DE-DA_Project
### An end to end data engineering and data analytics project

This project involves the use of the City Of Toronto's and Toronto Police KSI (Killed and Seriously Injured) dataset. This dataset contains various records and reports of automobile related collisions in the City of Toronto. More information regarding the dataset can be found here: https://open.toronto.ca/dataset/motor-vehicle-collisions-involving-killed-or-seriously-injured-persons/.

### Data Modelling

The dataset was first mapped into an ER model (instead of drawing keys and attributes protruding out the entity block like seen conventionally, I just included them in the entity block itself sort of like a uml table) and then converted into a relational model (both can be seen in data models folder). Some columns, not used in the dashboard, were not included. Please see the data_pipeline.ipynb file in the data engineering pipeline folder for information regarding the modelling process. 

![KSI Data Model (ER_v2)](https://github.com/user-attachments/assets/248cae47-c406-4d18-b52a-839c5a8221d2)
![KSI Data Model (Relational_new_v2)](https://github.com/user-attachments/assets/ebbee6eb-bccf-4620-a5fd-c1daaf90a040)



### Architecture
This project involves the Google Cloud Platform (GCP) tech stack, leveraging Mage.ai (https://www.mage.ai/) for building an ETL pipeline (see mage files folder), BigQuery for data warehousing, Looker Studio for data visualization (see dashboard under dashboard builder folder) and Google Cloud Storage for managing data. 

![architecture](https://github.com/user-attachments/assets/4b1607b6-a596-48c9-92c0-b0c40dc5d652)

### Dashboard

Alternatively you can see the dashboard here: https://lookerstudio.google.com/reporting/fefbf9ae-1f97-4909-96a9-7fa2bbddb75d




