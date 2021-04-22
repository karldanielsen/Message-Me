import json
import boto3
import os

def lambda_handler(event, context):
    client = boto3.client(
        "sns",
        region_name='us-east-1'
        )
    
    topic_arn = os.environ['sns_arn']
    status = client.publish(Message=json.loads(event['body'])["message"], TopicArn=topic_arn)['ResponseMetadata']['HTTPStatusCode']
    
    return {
        "isBase64Encoded": False,
        "statusCode": status,
        "headers": {
            "Access-Control-Allow-Origin": os.environ['CORS_headers'],
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Headers": "Content-Type",
            "Content-Type": "application/json",
            "body": "success!"
            }
    }
