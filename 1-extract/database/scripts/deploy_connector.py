import requests
import os

connector_config = {
  "name": "connector",  
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector", 
    "plugin.name":"pgoutput",
    "slot.name":os.getenv("SLOT_NAME"),
    "publication.name":os.getenv("PUBLICATION_NAME"),
    "database.hostname": "db", # match the name of the docker compose file 
    "database.port": "5432", 
    "database.user": os.getenv("DEBEZIUM_USER"), 
    "database.password": os.getenv("DEBEZIUM_PASSWORD"), 
    "database.dbname" : os.getenv("POSTGRES_DB"), 
    "topic.prefix": "connector",
    "topic.creation.default.replication.factor": 3,  
    "topic.creation.default.partitions": 3,
  }
}
headers = {
    "Accept":"application/json" ,
    "Content-Type":"application/json"
}

kafka_connect_api_url = "http://localhost:8083/connectors"
response = requests.post(kafka_connect_api_url,headers=headers,json=connector_config)

print(response.json())