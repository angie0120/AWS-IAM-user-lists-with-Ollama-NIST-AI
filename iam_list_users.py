import boto3
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="List IAM users in your AWS account.")            # Create a parser. This lets the script accept options like --profile or --details.
parser.add_argument("--profile", help="AWS profile name to use", default=None)                 # One option. This lets the user tell the script which AWS CLI profile to use, ex. --profile profilename.
parser.add_argument("--details", help="Show additional IAM user details", action="store_true") # Optional switch. If they type --details, the script will show extra information about each user.
args = parser.parse_args()                                                                     # Read whatever options the user typed and store them in 'args'.

# Create a session with AWS.
# If the user typed --profile profilename, use THAT profile.
# If they didn't type anything, fall back to their default AWS profile.
if args.profile:
    session = boto3.Session(profile_name=args.profile)
else:
    session = boto3.Session()

# Use the session to create an IAM client.
# This "client" is the Python interface to the IAM API, so we can call IAM functions like list_users().
iam = session.client("iam")

try:
    # List IAM users
    users = iam.list_users()

    print("List of IAM Users:")
    for user in users["Users"]:
        username = user["UserName"]
        created = user["CreateDate"].strftime("%Y-%m-%d %H:%M:%S")

        if args.details:
            arn = user["Arn"]
            user_id = user["UserId"]
            print(f"{username} | ID: {user_id} | ARN: {arn} | Created: {created}")
        else:
            print(f"{username} | Created: {created}")

except Exception as e:
    print(f"An error occurred: {e}")

