# Scripts-and-Automation

## AWS CLI Commands

### IAM Commands

Create and delete Iam users:
``aws iam create-user --user-name <UserName>``

``aws iam delete-user --user-name <UserName>``

Create a delete login profile and password:
``aws iam create-login-profile --user-name <UserName> --password <password>``

``aws iam delete-login-profile --user-name Alice``

Create and delete access keys:
``aws iam create-access-key --user-name Alice``


