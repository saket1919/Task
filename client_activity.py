import boto3

client = boto3.client('stepfunctions')
response = client.create_activity(
    name='string',
    tags=[
        {
            'key': 'string',
            'value': 'string'
        },
    ]
)
print(response)