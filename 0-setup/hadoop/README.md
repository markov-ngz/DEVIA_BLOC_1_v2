# Hadoop Cluster
Unsecure Hadoop Cluster setup with 1 namenode and 1 datanode
## Infrastructure
1. Set the following environment variables
```
export TF_VAR_public_ip="$(curl -s ifconfig.me)"
export TF_VAR_ec2_public_key="<public_key_path>"
export TF_VAR_key_name="aws_key_name"
```
2. Create the infra
```
terraform apply --auto-approve
```
## Setup 
On each machine , run the following ( don't forget to replace the hadoop value to your matching one ) : 
0. Install Java if not done 
```
sudo apt install default-jre
```
1. Download Hadoop and check hash value
```
# see for available downloads
curl -O https://dlcdn.apache.org/hadoop/common/hadoop-3.3.5/hadoop-3.3.5.tar.gz
# check hash 
gpg --print-md SHA512 hadoop-3.3.5.tar.gz
```
2. Unzip
```
tar -xf hadoop-3.3.5.tar.gz
```
3. Add Hadoop to your path
```
nano ~/.profile
>>
export HADOOP_HOME=<hadoop_path>/hadoop-3.3.5
export PATH="$HOME/<path>/hadoop-3.3.5/bin:$PATH"
<<
source ~/.profile
```
4. set $JAVA_HOME in hadoop-env.sh
```
nano $HADOOP_HOME/etc/hadoop/hadoop-env.sh
>>
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
<<
```
5. Allow SSH between datanode and namenode 
```
# create key 
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
# copy content of the public key and paste to the other machine's ~/.ssh/authorized_keys
# test localhost between the two 
```
## Namenode & Datanode Configuration
1. Copy and configure the values of the datanode/namenode's hdfs-site.xml and core-smite.xml to set it in place of the current namenode etc/hadoop/ default configuration
2. On the namenode run 
```
hdfs namenode -format
```
3. Run the namenode (check on namenode_public_ip:9870 to see if the web gui is present)
```
hdfs namenode
```
4. Format datanode
```
hdfs datanode -format
```
5. Run the datanode
```
hdfs datanode
```
On the web gui of the namenode, the datanode should be seen 
## Project setup
Run the following to create the necessary folders 
```
# Start cluster
cd $HADOOP_HOME

# Project Ingestion folder
hdfs dfs -mkdir /translations

# Organizing folders by source not by type of data
hdfs dfs -mkdir /translations/cassandra
hdfs dfs -mkdir /translations/web_scrapping
hdfs dfs -mkdir /translations/sftp

# Output folder to load the data
hdfs dfs -mkdir /translations/output

# Adjust permissions
hdfs dfs -chmod -R 777 /translations
```