from classAWSAccount import AWSAccount
from ec2 import ec2
from users import users

# boto3 for aws services
import boto3
session = boto3.Session(profile_name="eni", region_name="eu-central-1")
ec2_list = []


def main():
    cdp_account = AWSAccount("825880227928")  # pass access & secret keys
    # print(cdp_account.account_id)

    # create ec2 session
    ec2_client = session.client("ec2")
    instances = ec2_client.describe_instances()["Reservations"]
    for instance in instances:
        try:
            # get instance json file
            instance_name = instance["Instances"][0]["KeyName"]
            ami_id = instance["Instances"][0]["ImageId"]
            model = instance["Instances"][0]["InstanceType"]
            dns_name = instance["Instances"][0]["PrivateDnsName"]
            print(instance_name)
            print(ami_id)
            print(model)
            print(dns_name)

            cdp_ec2 = ec2(instance_name, ami_id, model, dns_name)
            ec2_list.append(cdp_ec2)
        except:
            cdp_ec2 = ec2("no name", ami_id, model, dns_name)
            ec2_list.append(cdp_ec2)

        for instance in ec2_list:
            print(instance)
    print()


main()
