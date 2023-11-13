
import boto3
import json
import pprint
from pymongo import MongoClient

# Initialize the AWS Pricing client for the 'us-east-1' region
pricing = boto3.client('pricing', region_name='us-east-1')

all_services = [] #has service code and its attributes
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


serviceCodeList=[]
for service in all_services:
    serviceCodeList.append(service['ServiceCode']) #we are only adding service code and not attributes

print(serviceCodeList)
f=0
c=0
for each in serviceCodeList:
    c+=1
    print(c,"",each," Products")
    #print("=====================")

    #c = 0  # Counter to track the number of products
    next_token = ""  # Initialize the NextToken as an empty string

    while True:
        # Use the get_products method to retrieve pricing information for the 'nimble' service
        response = pricing.get_products(
            ServiceCode=each,
            Filters=[
                {'Type': 'TERM_MATCH', 'Field': 'serviceCode', 'Value': each},
            ],
            NextToken=next_token  # Pass the NextToken to fetch the next page of results
        )
        #add to mongoDB
        # MongoDB connection string (replace with your own)
        connection_string = "mongodb://localhost:27017"

        # Database and collection names (replace with your own)
        db_name = "AWS"
        collection_name = 'aws_pricing'

        try:
            # Connect to MongoDB
            client = MongoClient(connection_string)

            # Access the database
            db = client[db_name]

            # Access the collection
            collection = db[collection_name]
            # Insert the JSON data into the collection
            for price in response['PriceList']:
                pp = json.loads(price)
                inserted_data = collection.insert_one(pp)
                f += 1
                #print(f)


        except Exception as e:
            print("Error:", e)
        finally:
            client.close()
        '''
        # Loop through the list of pricing information
        for price in response['PriceList']:
            pp = pprint.PrettyPrinter(indent=1, width=300)
            pp.pprint(json.loads(price))
            c += 1
            f+=1
            print(f)
            print()
'''
        # Check if there are more pages of results
        if 'NextToken' in response:
            next_token = response['NextToken']
        else:
            break

            c += 1
            #print(c)
            #print()

