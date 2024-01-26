import os

import boto3


client = boto3.client(
    "sqs",
    endpoint_url=os.environ.get("SQS_ENDPOINT"),
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    region_name=os.environ.get("AWS_DEFAULT_REGION"),
)


train_task_queue_url = client.get_queue_url(QueueName="training-task-queue")["QueueUrl"]
