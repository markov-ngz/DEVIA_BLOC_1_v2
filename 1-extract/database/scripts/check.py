"""Run these requests to check the configuration"""
import requests

# get status 
response_1 = requests.get("http://localhost:8083/",headers={"Accept":"application/json"})
print(response_1.json())

# get registered connectors 
response_2 = requests.get("http://localhost:8083/connectors/",headers={"Accept":"application/json"})
print(response_2.json())