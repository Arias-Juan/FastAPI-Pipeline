# GLOB-DE-Challenge

## Introduction
The process of resolve the challenge, were guided by the simple next cloud architecture:

![architecture](https://i.imgur.com/bhl84Ak.png)

This architecture is looking to resolve the next steps:  
1. Receive historical data from CSV files
2. Upload these files to the new DB
3. Be able to insert batch transactions (1 up to 1000 rows) with one reques

To consider the project were:
* Hosted in AWS Cloud, utilizing services like EC2 and S3 to minimize costs
* The api script were tested by Postman
* The project can be deployed by Docker with the Dockerfile in the repository
* The DB is public and can be access in any database management tool (eg. Dbeaver)
* All the scripts are updated with the first time from this GitHub repository

### CSV
The files are comma delimited and primary are:
* jobs.csv
* deparments.csv
* hired_employees.csv

### S3
The AWS S3 Bucket are created to utilize the minimium of capacity, with any load to the DB the API deleted the file in the bucket.

### EC2
The AWS EC2 services is configured to host a virtual server of a Linux Ubuntu system.  
It's configured to maintain the free tier cost in AWS plataform.

### Python Scripts
#### Trigger
#### API

### PostgreSQL

### Docker


## Backlog improvement
