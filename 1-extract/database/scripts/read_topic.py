"""In case you encounter some problems, read from the topic to see if indeed message are printed"""
from kafka import KafkaConsumer

topic_name = "connector.ref_sol_ail"
consumer = KafkaConsumer(topic_name,bootstrap_servers="localhost:9091")

for msg in consumer : 
    print(msg)