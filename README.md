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

### How to start
You must need to have installed git, docker and docker-compose in your instance.
```
git clone <this repository>
cd GLOB-DE-Challenge
vim/nano .env #create the variables like is show next
docker-compose up --build app trigger postgres
```
The .env file must have this variables:
- aws_access_key_id=<Token you obtain from aws console you needed to access s3>
- aws_secret_access_key=<Token you obtain from aws console you needed to access s3>
- user_psql=<The user to access postgres / must be modified in docker-compose.yml too>
- password_psql=<The password to access postgres / must be modified in docker-compose.yml too>
- DB_URL='jdbc:postgresql://<IP of your instance>:5432/challenge_db?currentSchema=public'
- API_URL='http://<IP of your instance>:8080'

#### CSV
The files are comma delimited and primary are:
* jobs.csv
* deparments.csv
* hired_employees.csv

#### S3
The AWS S3 Bucket are created to utilize the minimium of capacity, with any load to the DB the API deleted the file in the bucket.

#### EC2
The AWS EC2 services is configured to host a virtual server of a Linux Ubuntu system.  
It's configured to maintain the free tier cost in AWS plataform.

#### Python Scripts
There are two python scripts: Trigger and Main API.
Trigger is the script that watch the s3 bucket and when a file is loaded, do a call to the api to upload the file in postgres and then deleted the file.
Main API is the api that recive the call and make the action working with pyspark, pandas, request, amoung others libraries.

#### PostgreSQL
The PostgreSQL are configured to start a database called challenge_db, later in that database is where the API make the write of the extracted tables from s3.

#### Docker
The project use Docker and Docker-compose to build the containers with three apps: trigger, app and postgre, all in one image.

## Backlog improvement
- [ ] To future, according to cost, replace EC2 with AWS services like Lambda, Glue, DynamoDB and Cloudwatch.
- [ ] Change the load to transform the csv file to parquet (With Hudi).
- [ ] Friendly tables dictionary modification from a drive file.
- [ ] The POST to API can include a dictionary or model of the table.
- [ ] Parameters with en API call like "incremental" or "full" insert, name stored in db and specify type of file.
