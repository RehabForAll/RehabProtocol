import boto3
import json

# from boto.dynamodb2.table import Table

# For a Boto3 service resource
ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = ddb.Table('UUIPDPathology')

with open("/Users/jeremy/Desktop/Projects/Rehab Protocol/json.json") as file:
    data = json.load(file)


for i in data(data.UUID):
    print(i)
