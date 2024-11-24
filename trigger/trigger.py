from datetime import datetime
import boto3
import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')

s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name='sa-east-1'
)

api = "http://0.0.0.0:8080/test"

bucket_name = "glob-de-challenge"

log_file = "./log/watcher.log"
os.makedirs(os.path.dirname(log_file), exist_ok=True)

def check_new_files():
   response = s3_client.list_objects_v2(Bucket=bucket_name)
   if 'Contents' in response:
        files = [file['Key'] for file in response['Contents']]
        timestamp = datetime.now()
        watch_log = f'[WATCH] {timestamp}: File found "{files[0]}"'
        with open(log_file, 'a') as file:
          file.write(watch_log + "\n")
        return files[0]
   else:
        timestamp = datetime.now()
        watch_log = f'[WATCH] {timestamp}: No file load in the bucket'
        with open(log_file, 'a') as file:
          file.write(watch_log + "\n")
        return []

def call_api(file):
    timestamp = datetime.now()
    try:
        # Can apply post with dictionary in future
        response = requests.get(api)
        if response.status_code == 200:
            watch_log = f'[SUCCESS] {timestamp}: {file} load via API.'
            with open(log_file, 'a') as file:
              file.write(watch_log + "\n")
        else:
            watch_log = f'[ERROR] {timestamp}: {file} dont load.'
            with open(log_file, 'a') as file:
              file.write(watch_log + "\n")
    except Exception as e:
        watch_log = f'[ERROR] {timestamp}: API ERROR ({e}).'
        with open(log_file, 'a') as file:
          file.write(watch_log + "\n")

def monitor_s3_for_files():
    while True:
        file = check_new_files()

        if file:
            call_api(file)
            timestamp = datetime.now()
            s3_client.delete_object(Bucket=bucket_name, Key=file)
            watch_log = f'[DELETE] {timestamp}: Deleted {file} in bucket.'
            with open(log_file, 'a') as file:
              file.write(watch_log + "\n")
        
        time.sleep(60)

monitor_s3_for_files()
