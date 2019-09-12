# VPG Automation With Python 3 and Boto 3

## Requirements 
- Python 3 with Boto 3 Package

## Instructions 

1. Download the script from this repository
2. Create an IAM user/role that has access to make changes with ec2
3. Use the `aws config` command to enter the access key ID and secret access key to connect with the acount that you will create the VPG in
4. Run the command python3 `vpgautomation.py` 
5. Follow the prompts to create cgw and vpg for a vpn connection to an on premise site

### Notes
- There are a few more steps required on the AWS side to do that I will include in this script in order to automate as much as possible.
- There is a code in line 9 `filters = [{'Name': 'tag:Name', 'Values': ['Phones']}]` that is used in order to not include multiple VPCs in the json dump. If you have only one VPC that is untagged you can replace `'Phones'` with `'*'`
