import boto3
import botocore

print("My Enumerator")
print("=============")
accessiam = boto3.client('sts',region_name='us-west-2',aws_access_key_id='',aws_secret_access_key='')
print(accessiam.get_caller_identity())

