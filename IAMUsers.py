from users import users
#boto3 for aws services
import boto3
import csv

def main():
    # Create lists
    users_list = []
    userat = []
    arns = []
    session = boto3.Session(profile_name="eni", region_name="eu-central-1")
    # create iam session
    iam_client = session.client("iam")

    users1 = iam_client.list_users()["Users"]

    for user in users1:
        try:
            user_arn = user["Arn"]
            user_name = user["UserName"]
            cdp_user = users(user_arn, user_name)

            users_list.append(cdp_user)           
             # Add User Name and ARN to lists for CSV
            userat.append(cdp_user.get_name())
            arns.append(cdp_user.get_arn())            
            # Write users to a CSV file
            with open('users.csv', 'w', newline='') as csvfile:
                fieldnames = ['Name', 'ARN']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)                
                writer.writeheader()
                writer.writerow({'Name': userat, 'ARN': arns})
        except:
            print("no user")
    # Print all users
    for us in users_list:
        print(us)
main()
