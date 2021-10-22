import datetime
import json
import random
import boto3
from setting import *
import time


def get_data():
    return {
        'event_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'name': random.choice(['AAPL', 'AMZN', 'MSFT', 'GOOG', 'FB']),
        'price': round(random.random() * 2000 + 100, 2)}


def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey="partitionkey")
        time.sleep(SEND_INTERVAL * 0.001)


if __name__ == '__main__':
    session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_key)
    c = session.client('kinesis', region_name='cn-northwest-1')

    generate(STREAM_NAME, session.client('kinesis', region_name=REGION))
