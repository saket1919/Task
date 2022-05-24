import boto3
region = 'ap-south-1'

ec2 = boto3.client('ec2',
                   'ap-south-1',
                   aws_access_key_id='',
                   aws_secret_access_key='')

def list_instances():
    instance_ids = []
    response = ec2.describe_instances(Filters=[{'Name': 'instance-type', 'Values': ["t2.micro", "t3.micro"]}])
    instances_full_details = response['Reservations']
    for instance_detail in instances_full_details:
        group_instances = instance_detail['Instances']

        for instance in group_instances:
            instance_id = instance['InstanceId']
            instance_ids.append(instance_id)
    return instance_ids

instance_ids = list_instances()
print(instance_ids)