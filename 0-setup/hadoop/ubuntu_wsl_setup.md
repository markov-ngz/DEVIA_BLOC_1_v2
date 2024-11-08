# 1. Setup 
1. download binaries
```
curl -O https://dlcdn.apache.org/hadoop/common/hadoop-3.3.5/hadoop-3.3.5.tar.gz
```
2. Check SHA 512
```
gpg --print-md SHA512 hadoop-3.3.5.tar.gz
```
3. tar 
```
tar -xf hadoop-3.3.5.tar.gz
```
3. add hadoop to path & add hadoop_home
```
nano ~/.profile
>>
export HADOOP_HOME=<hadoop_path>/hadoop-3.3.5
export PATH="$HOME/bigdata/hadoop-3.3.5/bin:$PATH"
<<
source ~/.profile
```
4. set $JAVA_HOME in hadoop-env.sh
```
nano etc/hadoop/hadoop-env.sh
>>
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
<<
```
5. if !ssh localhost ? install openssh-server & add commands for key 
```
sudo apt-install openssh-server

ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
```
You should be able to run 
```
ssh localhost
```
# 2. Configuration 
1. Add the following to etc/core-site.xml
```
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```
2. Add the following to etc/hdfs-site.xml
```
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```
3. Format 
```
bin/hdfs namenode -format
```
# 3. Authorization
If you run scripts on windows, the user will differ from the WSL's root.
Hence you need to allow your user to hadoop's group
```
hdfs dfs -chmod 777 /
```
# 4. Run 
7. run hadoop 
```
sbin/start-dfs.sh
```
8. Check on WEB GUI ```http://localhost:9870`` `
