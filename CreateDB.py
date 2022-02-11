from AWSAccount import ec2_list
import boto3# Create session for Boto3 with aws profile credentials
boto3.setup_default_session(profile_name='eni', region_name="eu-central-1")
# Create a table named EC2-Table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    TableName='EC2-eni',
    # Add two keys
    KeySchema=[
        {
            'AttributeName': 'Name',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Ami',
            'KeyType': 'RANGE'
        }
    ],
    # Specify the type
    AttributeDefinitions=[
        {
            'AttributeName': 'Name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Ami',
            'AttributeType': 'S'
        },
    ],
    # Specify the Capacity
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)