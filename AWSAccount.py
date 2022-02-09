from classes.AWSAccount import AWSAccount
import boto3


def main():
  cdp_account = AWSAccount("825880227928")  # pass access & secret keys
  # print(cdp_account.account_id)

  import boto3
  boto3.Session()
  ec2_client = boto3.client('ec2',
                            aws_access_key_id="AKIA4ASSMGBMOHDYEUTW",
                            aws_secret_access_key="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",
                            region_name="eu-central-1")
  instances = ec2_client.describe_instances()["Reservations"]
  for instance in instances:
    try:
      instance_name = instance["Instances"][0]["KeyName"]
      ami_id = instance["Instances"][0]["ImageId"]
      model = instance["Instances"][0]["InstanceType"]
      dns_name = instance["Instances"][0]["PrivateDnsName"]
    except:
      print("no name")


main()