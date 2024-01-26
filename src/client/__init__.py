import os

import boto3


client = boto3.client("sqs", endpoint_url=os.environ.get("SQS_ENDPOINT"), region_name=os.environ.get("AWS_REGION"))

train_task_queue_url = client.get_queue_url(QueueName="training-task-queue")["QueueUrl"]
