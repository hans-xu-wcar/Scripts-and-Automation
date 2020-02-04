# Scripts-and-Automation

## AWS CLI Commands

### IAM Commands

**Create, delete and reset Iam users:**

- ``aws iam create-user --user-name <UserName>``

- ``aws iam delete-user --user-name <UserName>``

- ``aws iam update-login-profile --user-name <UserName> --password <password>``

**Create a delete login profile and password:**

- ``aws iam create-login-profile --user-name <UserName> --password <password>``

- ``aws iam delete-login-profile --user-name Alice``

**Create access keys:**

- ``aws iam create-access-key --user-name Alice``

**Create IAM Groups, Add User to Groups and List Users in Group:**

- ``aws iam create-group --group-name <groupName>``

- ``aws iam add-user-to-group --group-name <groupName> --user-name <userName>``

- ``aws iam get-group --group-name <groupName>``

- To list ONLY UserNames in a group: ``aws iam get-group --group-name <groupName> --query Users[*].UserName --output json``

## EC2 Commands
- List all EC2 instances ``aws ec2 describe-instances``
``aws ec2 terminate-instances --instance-id <id>``
- List all EC2 instances per Tag - ``aws ec2 describe-tags --query Tags[?ResourceType==`instance`] --output json``
- Launch EC2 - ``aws ec2 run-instances --image-id <ami> --count <integer> --instance-type <ex. t2.micro>``


## RDS Commands
- List all RDS Datbases ``aws rds describe-db-instance --region``

