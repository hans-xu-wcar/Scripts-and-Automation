# Scripts-and-Automation

## AWS CLI Commands

### IAM Commands

**Create, delete and reset Iam users:**

``aws iam create-user --user-name <UserName>``

``aws iam delete-user --user-name <UserName>``

``aws iam update-login-profile --user-name <UserName> --password <password>``

**Create a delete login profile and password:**

``aws iam create-login-profile --user-name <UserName> --password <password>``

``aws iam delete-login-profile --user-name Alice``

**Create access keys:**

``aws iam create-access-key --user-name Alice``

**Create IAM Groups and Add User to Groups:**

``aws iam create-group --group-name <groupName>``

``aws iam add-user-to-group --group-name <groupName> --user-name <userName>``

## EC2 Commands
``aws ec2 terminate-instances --instance-id <id>``




