# Hadoop Cluster
Local Setup of an Hadoop Cluster.
<ul>
<li>For single node cluster setup see file : <b>hadoop_setup.pdf</b></li>
<li>As a nexample of Spark application that can be used  : <b>bigdata_doc.pdf</b></li>
</ul>

<br>
The following covers a conteneurized simulation of a hadoop cluster with docker . 

## Containers 
HDFS (Hadoop Distributed File System):
<ul>
<li>Namenode : </li>
<li>Datanodes : </li>
</ul>
YARN (Yet Another Resource Manager):
<ul>
<li>Resource Manager : </li>
<li>Node Manager : </li>
</ul>

## Schema
<img src="" />

## Setup 
Run local cluster 
```
docker compose up -d
```
By default the host user is not authorized to perform file operation to the cluster as it is not auth and kerberos is also not set up :
Hence for development purpose , the ugly trick is done :  
```
docker exec namenode hdfs dfs -chown <host_user>:hadoop /
or 
docker exec namenode hdfs dfs -chmod -R 777 /
```
## Configuration
Documentation links :
- HDFS Ports : https://ambari.apache.org/1.2.4/installing-hadoop-using-ambari/content/reference_chap2_1.html 
- Full reference : https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml
Description about the environment variable used
```
HADOOP_HOME=/opt/hadoop

CORE-SITE.XML_fs.defaultFS=hdfs://namenode:8020 # namenode address the datanode will try to connect to 

HDFS-SITE.XML_dfs.namenode.rpc-address=namenode:8020 # rpc address from which the datanode will connect to namenode
HDFS-SITE.XML_dfs.replication=1

MAPRED-SITE.XML_mapreduce.framework.name=yarn
MAPRED-SITE.XML_yarn.app.mapreduce.am.env=HADOOP_MAPRED_HOME=$HADOOP_HOME
MAPRED-SITE.XML_mapreduce.map.env=HADOOP_MAPRED_HOME=$HADOOP_HOME
MAPRED-SITE.XML_mapreduce.reduce.env=HADOOP_MAPRED_HOME=$HADOOP_HOME

```
## Code Reference 
- docker-compose : 
https://medium.com/@bayuadiwibowo/deploying-a-big-data-ecosystem-dockerized-hadoop-spark-hive-and-zeppelin-654014069c82