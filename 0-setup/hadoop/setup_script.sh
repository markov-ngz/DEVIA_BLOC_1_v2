# Start cluster
cd $HADOOP_HOME
hdfs namenode -format
sbin/start-dfs.sh

# Organizing folders by source not by type of data
hdfs dfs -mkdir /cassandra
hdfs dfs -mkdir /web_scrapping
hdfs dfs -mkdir /sftp

# Adjust permissions
hdfs dfs -chmod -R 777 /