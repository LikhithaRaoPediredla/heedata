#code to get all regions and services available

import boto3

# Replace 'your-region-name' with the appropriate AWS region, e.g., 'us-east-1'
pricing = boto3.client('pricing', region_name='us-east-1')

# Call describe_services() with pagination
all_services = []
next_token = None

while True:
    params = {}
    if next_token:
        params['NextToken'] = next_token

    response = pricing.describe_services(**params)
    all_services.extend(response['Services'])

    next_token = response.get('NextToken')
    if not next_token:
        break

# Now 'all_services' contains information about all available services
c = 0

for service in all_services:
    # service is dictionary with 2 keys: servicecode and Attributes
    c += 1
    sc = service['ServiceCode']
    print("\nSelected", sc, "Attributes & Values")
    print("================================")

    response = pricing.describe_services(ServiceCode=sc)
    # response is dict with following dict_keys(['Services', 'FormatVersion', 'ResponseMetadata'])
    # services is the first key which holds a list

    attrs = response['Services'][0]['AttributeNames']
    # services is the first key which contains a list having a dictionary with 2 keys: ServiceCodes(variable),AttributeNames(list)

    for attr in attrs:
        response = pricing.get_attribute_values(ServiceCode=sc, AttributeName=attr)
        # what is response here what all keys
        values = []
        for attr_value in response['AttributeValues']:
            values.append(attr_value['Value'])

        print("  " + attr + ": " + ", ".join(values))
print(c)


"""
#code to get services and their respective attributes
import boto3

# Replace 'your-region-name' with the appropriate AWS region, e.g., 'us-east-1'
pricing = boto3.client('pricing', region_name='us-east-1')

# Call describe_services() with pagination
all_services = []
next_token = None

while True:
    params = {}
    if next_token:
        params['NextToken'] = next_token

    response = pricing.describe_services(**params)
    all_services.extend(response['Services'])

    next_token = response.get('NextToken')
    if not next_token:
        break

# Now 'all_services' contains information about all available services
print(all_services)
c=0

for service in all_services:
    c+=1
    print(service['ServiceCode'] + ": " + ", ".join(service['AttributeNames']))
    print()
print(c)


#code to get attributes and their values given a service

import boto3
import json
import pprint

pricing = boto3.client('pricing',region_name='us-east-1')

print("Selected S3 Attributes & Values")
print("================================")
response = pricing.describe_services(ServiceCode='AmazonS3')

attrs = response['Services'][0]['AttributeNames']


for attr in attrs:
    response = pricing.get_attribute_values(ServiceCode='AmazonS3', AttributeName=attr)
    #response is a dict,attributeValues is the key in the dict

    values = []
    for attr_value in response['AttributeValues']:
        values.append(attr_value['Value'])

    print("  " + attr + ": " + ", ".join(values))
"""
