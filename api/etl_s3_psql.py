from fastapi import APIRouter
from dotenv import load_dotenv
import boto3
from tables_dictionary import schemas
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import col,lit
import pandas as pd
from io import StringIO

spark = SparkSession.builder.appName("etl_s3_psql").config("spark.jars", './lib/postgresql-42.7.1.jar').getOrCreate()

load_dotenv()
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')

s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name='sa-east-1'
)

url = "jdbc:postgresql://0.0.0.0:5432/challenge_db"
properties = {
    "user": os.getenv('user_psql'),
    "password": os.getenv('password_psql'),
    "driver": "org.postgresql.Driver"
}

bucket_name = 'glob-de-challenge'

etl_s3_psql = APIRouter()

@etl_s3_psql.get(f'/{table}')
async def root():
	response = s3_client.get_object(Bucket=bucket_name, Key=f'{table}.csv')
	csv_raw = response['Body'].read().decode('utf-8')
	pandas_df = pd.read_csv(StringIO(csv_raw))
	if schemas[table]:
		df = spark.createDataFrame(pandas_df, schema=schemas[table])
	else:
		df = spark.createDataFrame(pandas_df)
	try:
    	df.write.jdbc(url, table, mode="overwrite", properties=properties)
    	return {"Table_load": table}
	except Exception as e:
    	return {"Table_error": e}