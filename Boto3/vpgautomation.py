import json
import boto3
import boto.vpc

ec2 = boto3.resource('ec2', region_name='us-east-1')
client = boto3.client('ec2')


# add tags later
filters = [{'Name': 'tag:Name', 'Values': ['*']}]

vpcs = list(ec2.vpcs.filter(Filters=filters))

for vpc in vpcs:
    response = client.describe_vpcs(
        VpcIds=[
            vpc.id,
        ]
    )
    #print(json.dumps(response, sort_keys=True, indent=4))

VPCforVPN = vpc.id
# print(VPCforVPN)

conn = boto.vpc.connect_to_region('us-east-1')

print("Please enter the customer public IP address")

onPremPublic = raw_input()

##Can this be cleaner???###
if (len(onPremPublic)) >= 7 and (len(onPremPublic)) <= 15:
    print("Thank you!")
elif (len(onPremPublic)) >= 16 or (len(onPremPublic)) < 7:
    print("Invalid Entry")

#print(len(onPremPublic))

CustomerGateway = conn.create_customer_gateway('ipsec.1',onPremPublic,'65534')
print(CustomerGateway.id)

VPN = conn.create_vpn_gateway('ipsec.1')
print(VPN.id)

#Attach VPN to VPC
VirtualGateway = VPN.attach(VPCforVPN)
print(VirtualGateway.id)

a = type(VirtualGateway)
print(a)
print(VirtualGateway)

VpnConnect = conn.create_vpn_connection('ipsec.1',CustomerGateway.id,VirtualGateway.id)
print(VpnConnect)
