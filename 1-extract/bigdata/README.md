# Requêtes d'un système big data

# Configuration
Apache Cassandra est une application Java (JDK doit donc e^tre installé). 
Afin d'exécuter les requêtes par le langage CQLSH, Python est aussi nécessaire.
## Connectivité 
Apache Cassandra utilise 3 ports :
- 7000 : port du protocole Gossip (communication inter-node)
- 7199 : port des métriques au format JMX de la JVM
- 9042 : écoute des requêtes au port 9042
## Multi Node
SEED : 
## Help
liens utiles: 
- https://medium.com/@kayvan.sol2/deploying-apache-cassandra-cluster-3-nodes-with-docker-compose-3634ef8345e8
- https://www.youtube.com/playlist?list=PLn6POgpklwWqNNhhGIJyArMm-rDeGoZs1
