import boto3


client = boto3.client('s3', region_name='ap-south-1')
paginator = client.get_paginator('list_objects')
response_iterator = paginator.paginate(
 PaginationConfig={
     'MaxItems': 1000,
     'PageSize': 123},Bucket='')
for page in response_iterator:
    u = page['Contents']
    for user in u:
        print(user)