from AWSAccount import ec2_list
import boto3
boto3.setup_default_session(profile_name='eni', region_name="eu-central-1")

# Assign the previous created table to be used
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('EC2-eni')# Add table Items
table.put_item(
    Item={
        'Name': ec2_list[0].name,
        'Ami': ec2_list[0].ami,
        'Instance Type': ec2_list[0].model,
        'Dns': ec2_list[0].dns,
    }
)
table.put_item(
    Item={
        'Name': ec2_list[1].name,
        'Ami': ec2_list[1].ami,
        'Instance Type': ec2_list[1].model,
        'Dns': ec2_list[1].dns,
    }
)

