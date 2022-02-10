from classAWSAccount import AWSAccount
from users import users

import boto3
session = boto3.Session(profile_name="eni",region_name="eu-central-1")

def main():
  cdp_account = AWSAccount("825880227928")  # pass access & secret keys
  # print(cdp_account.account_id)

  
  ec2_client = session.client("ec2")
  instances = ec2_client.describe_instances()["Reservations"]
  for instance in instances:
    try:
      instance_name = instance["Instances"][0]["KeyName"]
      ami_id = instance["Instances"][0]["ImageId"]
      model = instance["Instances"][0]["InstanceType"]
      dns_name = instance["Instances"][0]["PrivateDnsName"]
      print(instance_name)
      print(ami_id)
      print(model)
      print(dns_name)
    except:
      print("no name")


iam_client= session.client("iam")
users1 =iam_client.list_users()["Users"]  
for user in users1:
    try:
     user_arn = user["Arn"]
     user_name = user["UserName"]      
     cdp_user = users(user_arn,user_name)
     print(cdp_user.name)
    except:
        print("no user")


main()