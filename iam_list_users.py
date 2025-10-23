import boto3
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="List IAM users in your AWS account.")
parser.add_argument("--profile", help="AWS profile name to use", default=None)
parser.add_argument("--details", help="Show additional IAM user details", action="store_true")
args = parser.parse_args()

# Create session (use profile if provided)
if args.profile:
    session = boto3.Session(profile_name=args.profile)
else:
    session = boto3.Session()

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

