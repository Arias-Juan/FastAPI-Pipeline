from datetime import datetime
import boto3
import requests
import os
import time
from dotenv import load_dotenv
import logging

load_dotenv()
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')

s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name='sa-east-1'
)

api = os.getenv('API_URL')

bucket_name = "glob-de-challenge"

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_new_files():
   response = s3_client.list_objects_v2(Bucket=bucket_name)
   logging.debug("Running check_new_files")
   if 'Contents' in response:
        file_max = max(response['Contents'], key=lambda x: x['LastModified'])
        file = file_max['Key']
        timestamp = datetime.now()
        logging.info(f'File found: {file}.')
        return file
   else:
        timestamp = datetime.now()
        logging.warning("File dont found.")
        return []

def call_api(file):
    timestamp = datetime.now()
    file_api = os.path.splitext(file)[0]
    try:
        # Can apply post with dictionary in future
        response = requests.post(f'{api}/extract',json={"table": file_api})
        if response.status_code == 200:
            logging.debug("Success call to the API")
            file_error = False
        else:
            logging.error("Problem loading the file to the API")
            file_error = True
    except Exception as e:
        logging.critical(f'Problem with connection to the API: {e}')

def monitor_s3_for_files():
    while True:
        file = check_new_files()

        if file:
            call_api(file)
            timestamp = datetime.now()
            if file_error:
                file_error = False
                # Here can be added a function to notify what file has error to action.
                logging.critical("There is a problem in the file, please checkout.")
            else:
                s3_client.delete_object(Bucket=bucket_name, Key=file)
                logging.debug("File deleted successfully.")
        
        time.sleep(60)

monitor_s3_for_files()
