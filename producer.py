from datetime import datetime, timedelta
import json
import random
import boto3
from setting import *
import time


def get_price_data(interval):
    ts = datetime.now() + timedelta(seconds=interval) + timedelta(days=-2)
    return {
        'partition_key': "{0}/{1}".format(random.choice(['ORDER', 'FINANCE']), ts.strftime("%Y/%m/%d")),
        'type': random.choice(['ORDER', 'FINANCE']),
        'year': ts.strftime("%Y"),
        'month': ts.strftime("%m"),
        'day': ts.strftime("%d"),
        'event_time': ts.strftime("%Y-%m-%d %H:%M:%S"),
        'name': random.choice(['AAPL', 'AMZN', 'MSFT', 'GOOG', 'FB']),
        'price': round(random.random() * 2000 + 100, 2)}


if __name__ == '__main__':
    session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    kinesis_client = session.client('kinesis', region_name=REGION)

    while True:
        interval1 = random.randint(0, 10) - 5
        data1 = get_price_data(interval1)
        status1 = kinesis_client.put_record(
            StreamName=STREAM_NAME,
            Data=json.dumps(data1),
            PartitionKey=data1["partition_key"])
        print(status1)
        time.sleep(SEND_INTERVAL / 1000)
