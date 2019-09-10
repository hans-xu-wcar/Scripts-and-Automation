import json
import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')
client = boto3.client('ec2')


# add tags later
filters = [{'Name': 'tag:Name', 'Values': ['Phones']}]

vpcs = list(ec2.vpcs.filter(Filters=filters))

for vpc in vpcs:
    response = client.describe_vpcs(
        VpcIds=[
            vpc.id,
        ]
    )
    #print(json.dumps(response, sort_keys=True, indent=4))
    # print(vpc.id)

print("Please enter the customer public IP address")

publicipaddress = input()
print(publicipaddress)

if (len(publicipaddress)) >= 7 and (len(publicipaddress)) <= 15:
    print("Thank you!")
else:
    print("Error")
    raise ValueError('invalid ip address')

print("completed")

# Create Customer Gateway

operation_result1 = ec2.meta.client.create_customer_gateway(
    Type='ipsec.1', PublicIp=publicipaddress, BgpAsn=65534)

# Create VPN Gateway

operation_result2 = ec2.meta.client.create_vpn_gateway(Type='ipsec.1')
try:
    gateway_id = operation_result2['VpnGateway']['VpnGatewayId']
    ec2.meta.client.attach_vpn_gateway(VpcId=vpc.id, VpnGatewayId=gateway_id)

    ec2.create_tags(Tags=TAGS, Resources=[gateway_id])
except KeyError:
    print('Failed to create VPN gateway.')
