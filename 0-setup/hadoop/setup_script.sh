# Start cluster
cd $HADOOP_HOME
hdfs namenode -format
sbin/start-dfs.sh

# Project Ingestion folder
hdfs dfs -mkdir /translations

# Organizing folders by source not by type of data
hdfs dfs -mkdir /translations/cassandra
hdfs dfs -mkdir /translations/web_scrapping
hdfs dfs -mkdir /translations/sftp

# Adjust permissions
hdfs dfs -chmod -R 777 /translations