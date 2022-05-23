import boto3
import json

ssm = boto3.client('ssm')
s3 = boto3.client('s3')

response = ssm.get_parameter(
    Name='UserName'
    # WithDecryption=True|False
)

# paramDetails = {}

# paramDetails['UserName'] = response['Parameter']['Value']

s3_resp = s3.put_object(
    Body=f"UserName: {response['Parameter']['Value']}",
    Bucket='exercise-lambda-s3',
    Key='paramDetails.txt'
) 
