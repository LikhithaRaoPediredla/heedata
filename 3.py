

#print("Total services:", c)

"""
print("Selected awsc Products")
print("=====================")

next_token = ""  # Initialize NextToken as None to start the first page of results

c = 0  # Initialize the counter for total results

while True:
    # Fetch pricing data for Amazon S3 with pagination
    response = pricing.get_products(
        ServiceCode='AmazonCloudWatch',
        Filters=[
            {'Type': 'TERM_MATCH', 'Field': 'serviceCode', 'Value': 'AmazonCloudWatch'},
        ],
        NextToken=next_token
    )

    # Loop through the PriceList in the response
    for price in response['PriceList']:
        c += 1
        pp = pprint.PrettyPrinter(indent=1, width=300)
        pp.pprint(json.loads(price))

        print()

    # Check if there are more pages of results
    next_token = response.get('NextToken')

    if not next_token:
        break  # Exit the loop if there are no more pages

print(c)"""

"""import boto3
import json
import pprint

pricing = boto3.client('pricing', region_name='us-east-1')

print("Selected EC2 Products")
print("=====================")

response = pricing.get_products(
     ServiceCode='AmazonEC2',
     Filters = [
         {'Type' :'TERM_MATCH', 'Field':'serviceCode', 'Value':'AmazonEC2'              },

     ],
     MaxResults=100
)

for price in response['PriceList']:
 pp = pprint.PrettyPrinter(indent=1, width=300)
 pp.pprint(json.loads(price))
 print()


import boto3

pricing = boto3.client('pricing', region_name='us-east-1')

# Call describe_services() with pagination
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

c=0
serviceCodeList=[]
for service in all_services:
    c+=1
    print()
    serviceCodeList.append(service['ServiceCode'])  #we are only adding service code and not attributes

print(c)
print(serviceCodeList)


"""





"""
#produces service names
import boto3

# Initialize the AWS Service Quotas client
client = boto3.client('service-quotas',region_name='us-east-1')

try:
    # Initialize the NextToken
    next_token = None
    c = 0
    while True:
        # List services
        params = {}
        if next_token:
            params['NextToken'] = next_token

        response = client.list_services(**params)

        # Extract and print service names and service codes
        for service in response['Services']:
            c+=1
            service_name = service['ServiceName']

            print(f"Service Name: {service_name}")

        # Check for pagination, if there is a NextToken, continue
        if 'NextToken' in response:
            next_token = response['NextToken']
        else:
            break
    print(c)
except Exception as e:
    print(f"An error occurred: {str(e)}")



"""



"""
import boto3

# Initialize the AWS Service Catalog client
client = boto3.client('servicecatalog',region_name='us-east-1')

# List portfolios
portfolios = client.list_portfolios()

# Iterate through portfolios and list service codes
for portfolio in portfolios['PortfolioDetails']:
    portfolio_id = portfolio['Id']

    # List organization access to the portfolio
    response = client.list_organization_portfolio_access(PortfolioId=portfolio_id)

    # Extract and print service names and codes
    for organization_access in response['OrganizationNodes']:
        for service_detail in organization_access['Services']:
            service_name = service_detail['ServiceName']
            service_code = service_detail['ServiceCode']

            print(f"Service Name: {service_name}, Service Code: {service_code}")
            
            
#code to get regions and service names
#table 1:aws_regions_services_

import boto3
import sqlite3

service_lookup = {
    "acm": "AWS Certificate Manager (ACM)",
    "acm-pca": "AWS Certificate Manager Private Certificate Authority (ACM PCA)",
    "alexaforbusiness": "Alexa for Business",
    "amplify": "AWS Amplify",
    "amplifybackend": "AWS Amplify Backend Environment",
    "amplifyuibuilder": "AWS Amplify UI Builder",
    "apigateway": "Amazon API Gateway",
    "appconfig": "Amazon AppConfig",
    "appflow": "Amazon AppFlow",
    "appinteg": "AWS AppIntegrations",
    "appmesh": "AWS App Mesh",
    "appstream": "Amazon AppStream",
    "appsync": "AWS AppSync",
    "athena": "Amazon Athena",
    "auditmanager": "AWS Audit Manager",
    "autoscaling": "AWS Auto Scaling",
    "awsconnector": "AWS Connector",
    "backup": "AWS Backup",
    "batch": "AWS Batch",
    "braket": "Amazon Braket",
    "budgets": "AWS Budgets",
    "chime": "Amazon Chime",
    "clouddirectory": "Amazon Cloud Directory",
    "cloudformation": "AWS CloudFormation",
    "cloudfront": "Amazon CloudFront",
    "cloudhsm": "AWS CloudHSM",
    "cloudsearch": "Amazon CloudSearch",
    "cloudtrail": "AWS CloudTrail",
    "cloudwatch": "Amazon CloudWatch",
    "codeartifact": "AWS CodeArtifact",
    "codebuild": "AWS CodeBuild",
    "codecommit": "AWS CodeCommit",
    "codedeploy": "AWS CodeDeploy",
    "codepipeline": "AWS CodePipeline",
    "codestar": "AWS CodeStar",
    "codestarconnections": "AWS CodeStar Connections",
    "codestar-notifications": "AWS CodeStar Notifications",
    "cognito-identity": "Amazon Cognito Identity",
    "cognito-idp": "Amazon Cognito User Pools",
    "comprehend": "Amazon Comprehend",
    "comprehendmedical": "Amazon Comprehend Medical",
    "compute-optimizer": "AWS Compute Optimizer",
    "config": "AWS Config",
    "connect": "Amazon Connect",
    "connect-contact-lens": "Amazon Connect Contact Lens",
    "connectparticipant": "Amazon Connect Participant",
    "cur": "AWS Cost and Usage Report Service",
    "dataexchange": "AWS Data Exchange",
    "datapipeline": "AWS Data Pipeline",
    "datasync": "AWS DataSync",
    "dax": "Amazon DynamoDB Accelerator (DAX)",
    "detective": "Amazon Detective",
    "devicefarm": "AWS Device Farm",
    "devopsguru": "Amazon DevOps Guru",
    "directconnect": "AWS Direct Connect",
    "discovery": "AWS Application Discovery Service",
    "dlm": "Amazon Data Lifecycle Manager",
    "dms": "AWS Database Migration Service",
    "ds": "AWS Directory Service",
    "dynamodb": "Amazon DynamoDB",
    "ec2": "Amazon Elastic Compute Cloud (EC2)",
    "ec2-instance-connect": "Amazon EC2 Instance Connect",
    "ecr": "Amazon Elastic Container Registry (ECR)",
    "ecs": "Amazon Elastic Container Service (ECS)",
    "efs": "Amazon Elastic File System (EFS)",
    "eks": "Amazon Elastic Kubernetes Service (EKS)",
    "elastic-inference": "Amazon Elastic Inference",
    "elasticache": "Amazon ElastiCache",
    "elasticbeanstalk": "AWS Elastic Beanstalk",
    "elastictranscoder": "Amazon Elastic Transcoder",
    "elb": "Elastic Load Balancing",
    "emr": "Amazon EMR",
    "es": "Amazon Elasticsearch Service (Amazon ES)",
    "eventbridge": "Amazon EventBridge",
    "fms": "AWS Firewall Manager",
    "forecast": "Amazon Forecast",
    "frauddetector": "Amazon Fraud Detector",
    "fsx": "Amazon FSx",
    "gamelift": "Amazon GameLift",
    "glacier": "Amazon S3 Glacier",
    "globalaccelerator": "AWS Global Accelerator",
    "glue": "AWS Glue",
    "greengrass": "AWS IoT Greengrass",
    "groundstation": "AWS Ground Station",
    "guardduty": "Amazon GuardDuty",
    "health": "AWS Health",
    "honeycode": "Amazon Honeycode",
    "iam": "AWS Identity and Access Management (IAM)",
    "identitystore": "Amazon Identity Store",
    "imagebuilder": "EC2 Image Builder",
    "inspector": "Amazon Inspector",
    "iot": "AWS IoT Core",
    "iot1click-devices": "AWS IoT 1-Click Devices Service",
    "iot1click-projects": "AWS IoT 1-Click Projects",
    "iotanalytics": "AWS IoT Analytics",
    "iotevents": "AWS IoT Events",
    "iotevents-data": "AWS IoT Events Data",
    "iot-jobs-data": "AWS IoT Jobs Data Plane",
    "iotthingsgraph": "AWS IoT Things Graph",
    "iotwireless": "AWS IoT Core for LoRaWAN",
    "ivs": "Amazon Interactive Video Service",
    "kafka": "Amazon Managed Streaming for Apache",
    "kendra": "Amazon Kendra",
    "kinesis": "Amazon Kinesis",
    "kinesisvideo": "Amazon Kinesis Video Streams",
    "kms": "AWS Key Management Service (KMS)",
    "lakeformation": "AWS Lake Formation",
    "lambda": "AWS Lambda",
    "lex": "Amazon Lex",
    "license-manager": "AWS License Manager",
    "lightsail": "Amazon Lightsail",
    "location": "Amazon Location Service",
    "logs": "Amazon CloudWatch Logs",
    "lookoutequipment": "Amazon Lookout for Equipment",
    "lookoutmetrics": "Amazon Lookout for Metrics",
    "lookoutvision": "Amazon Lookout for Vision",
    "machinelearning": "Amazon Machine Learning",
    "macie": "Amazon Macie",
    "managedblockchain": "Amazon Managed Blockchain",
    "marketplace-catalog": "AWS Marketplace Catalog",
    "mediaconnect": "AWS Elemental MediaConnect",
    "mediaconvert": "AWS Elemental MediaConvert",
    "medialive": "AWS Elemental MediaLive",
    "mediapackage": "AWS Elemental MediaPackage",
    "mediapackage-vod": "AWS Elemental MediaPackage VOD",
    "mediastore": "AWS Elemental MediaStore",
    "mediatailor": "AWS Elemental MediaTailor",
    "mgh": "AWS Migration Hub",
    "migrationhub-config": "AWS Migration Hub Config",
    "mobile": "AWS Mobile Hub",
    "mq": "Amazon MQ",
    "mturk": "Amazon Mechanical Turk",
    "neptune": "Amazon Neptune",
    "networkmanager": "AWS Network Manager",
    "opsworks": "AWS OpsWorks",
    "opsworkscm": "AWS OpsWorks CM",
    "organizations": "AWS Organizations",
    "outposts": "AWS Outposts",
    "panorama": "AWS Panorama",
    "personalize": "Amazon Personalize",
    "polly": "Amazon Polly",
    "pricing": "AWS Price List Service",
    "qldb": "Amazon Quantum Ledger Database (Amazon QLDB)",
    "quicksight": "Amazon QuickSight",
    "ram": "AWS Resource Access Manager",
    "rds": "Amazon RDS",
    "rds-data": "AWS RDS Data Service",
    "redshift": "Amazon Redshift",
    "rekognition": "Amazon Rekognition",
    "resourcegroupstaggingapi": "AWS Resource Groups Tagging API",
    "robomaker": "AWS RoboMaker",
    "route53": "Amazon Route 53",
    "route53domains": "Amazon Route 53 Domains",
    "route53resolver": "Amazon Route 53 Resolver",
    "s3": "Amazon Simple Storage Service (S3)",
    "s3control": "Amazon S3 Control",
    "sagemaker": "Amazon SageMaker",
    "sagemaker-a2i-runtime": "Amazon Augmented AI Runtime",
    "savingsplans": "Savings Plans",
    "schemas": "AWS Schemas",
    "secretsmanager": "AWS Secrets Manager",
    "securityhub": "AWS Security Hub",
    "serverlessrepo": "AWS Serverless Application Repository",
    "service-quotas": "Service Quotas",
    "servicecatalog": "AWS Service Catalog",
    "servicediscovery": "AWS Cloud Map",
    "ses": "Amazon Simple Email Service (Amazon SES)",
    "shield": "AWS Shield",
    "signer": "AWS Signer",
    "sms": "AWS Server Migration Service (SMS)",
    "sms-voice": "Amazon Pinpoint SMS and Voice Service",
    "snowball": "AWS Snowball",
    "s3outposts": "Amazon S3 on Outposts",
    "sqs": "Amazon SQS",
    "ssm": "AWS Systems Manager",
    "ssm-contacts": "AWS Systems Manager Contacts",
    "ssm-incidents": "AWS Systems Manager Incident Manager",
    "sso": "AWS Single Sign-On (AWS SSO)",
    "sso-admin": "AWS Single Sign-On (AWS SSO) Admin Operations",
    "sso-oidc": "AWS Single Sign-On (AWS SSO) OpenID Connect Provider",
    "states": "AWS Step Functions",
    "storagegateway": "AWS Storage Gateway",
    "sts": "AWS Security Token Service (STS)",
    "support": "AWS Support",
    "swf": "Amazon SWF",
    "synthetics": "Amazon CloudWatch Synthetics",
    "textract": "Amazon Textract",
    "transcribe": "Amazon Transcribe",
    "transfer": "AWS Transfer for SFTP",
    "translate": "Amazon Translate",
    "trustedadvisor": "AWS Trusted Advisor",
    "waf": "AWS WAF",
    "waf-regional": "AWS WAF Regional",
    "wafv2": "AWS WAFV2",
    "wellarchitected": "AWS Well-Architected Tool",
    "workdocs": "Amazon WorkDocs",
    "worklink": "Amazon WorkLink",
    "workmail": "Amazon WorkMail",
    "workmailmessageflow": "Amazon WorkMail Message Flow",
    "workspaces": "Amazon WorkSpaces",
    "xray": "AWS X-Ray"
    # Add more service codes and names as needed
}



# Create or connect to the SQLite database
conn = sqlite3.connect('aws_regions_services_.db')
cursor = conn.cursor()

# Create a table to store region and service data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS aws_data (
        id INTEGER PRIMARY KEY,
        region TEXT,
        service TEXT
    )
''')
conn.commit()

def list_regions_and_services():
    regions = boto3.session.Session().get_available_regions('ec2')
    region_count=0

    for region in regions:
        service_count = 0
        session = boto3.Session(region_name=region)
        available_services = session.get_available_services()
        print(f"Region: {region}")
        region_count+=1
        for service in available_services:
            # Insert region and service data into the SQLite database
            if service in service_lookup:
                service_count+=1
                k= service_lookup[service]
                print(f"- {k}")
                cursor.execute('INSERT INTO aws_data (region, service) VALUES (?, ?)', (region, k))
                conn.commit()
        print("region_count",region_count)
        print("service_count", service_count)

if __name__ == "__main__":
    list_regions_and_services()

    # Close the database connection when done
    conn.close()
            """

