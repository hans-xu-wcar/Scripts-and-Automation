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
    #print(vpc.id)

VPCforVPN = vpc.id
print(VPCforVPN)

#conn = boto3.VPCforVPN.connect_to_region('us-east-1')

print("Please enter the customer public IP address")

ipaddress = input()
print(ipaddress)

if (len(ipaddress)) >= 7 and (len(ipaddress)) <= 15:
    print("Thank you!")
else:
  print("Error")
  raise ValueError('invalid ip address')

print("completed")

#print(len(onPremPublic))

#CustomerGateway = conn.create_customer_gateway('ipsec.1',onPremPublic,'65534')
#print(CustomerGateway.id)

internetgateway = ec2.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=internetgateway.id)

#VPN = conn.create_vpn_gateway('ipsec.1')
#print(VPN.id)

#Attach VPN to VPC
#VirtualGateway = VPN.attach(VPCforVPN)
#print(VirtualGateway.id)

#a = type(VirtualGateway)
#print(a)
#print(VirtualGateway)

#VpnConnect = conn.create_vpn_connection('ipsec.1',CustomerGateway.id,VirtualGateway.id)
#print(VpnConnect)
