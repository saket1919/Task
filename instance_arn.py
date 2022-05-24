import boto3

sts = boto3.client('s3','ap-south-1')

region = boto3.Session().region_name

instance_id=''

account_id = sts.s3.get_caller_identity()['Account']

instance_arn=f"arn:aws:s3:{region}:{account_id}:instance/{instance_id}"

print(instance_arn)