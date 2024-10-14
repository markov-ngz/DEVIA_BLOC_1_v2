## Troubleshooting commands 
- Brokers :
```
# Create a topic  
./bin/kafka-topics.sh --create --bootstrap-server broker1:9092 --topic <topic_name> --replication-factor 3

# Describe topic 
./bin/kafka-topics.sh --describe --bootstrap-server broker1:9092 --topic <topic_name>

# Product into a topic 
./bin/kafka-console-producer.sh --topic <topic_name> --bootstrap-server broker1:9092

# Consum into a topic 
./bin/kafka-console-consumer.sh  --topic <topic_name> --bootstrap-server broker1:9092 --consumer-property group.id=<group_name>

# List consumer group state
./bin/kafka-consumer-groups.sh --bootstrap-server broker1:9092 --group <group_name> --describe
```
- Zookeeper : 
```
# Connect to cluster 
./bin/zkCli.sh -server zookeeper:2181

# Get brokers's id
ls brokers/id

# Get topics 
ls /brokers/topics

# Get broker's status 
get /brokers/ids/<id>

# Notes : the same can be done from within a broker 
./bin/zookeeper-shell.sh zookeeper:2181 ls /brokers/ids 
```