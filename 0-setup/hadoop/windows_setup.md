# Hadoop Pseudo Distributed Mode setup(Windows)
Installation of hadoop version 3.3.5 ( 5th of November 2024 )

## Prerequisites
This assume you have Java Installed which can be invoked by the commansd ```java --version```

## Hadoop Download
1. With your browser , download Hadoop tar.gz file  from following url : https://dlcdn.apache.org/hadoop/common/ 
2. Check the hash with the content of tar.gz.sha512 : ```certUtil -hashfile <path downloaded>.tar.gz  SHA512``` 
3. Extract the content : ```tar -xf <path>.tar.gz <to_path>```
4. Add hadoop-<ver>/bin directory to PATH 
5. For user , add a new variable JAVA_HOME to the user's : ```C:\Progra~1\Java\jdk-<javaver>``` ( a bug occures on windows for Program Files folder because the folder contains a space , hence you need to add ~1 )

## Hadoop Configuration
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
3. BLOCKED as no binaries are available or compiling is such an ass zzz
## Reference
- Windows Install : https://medium.com/@rebaimaha/guide-complet-pour-d%C3%A9buter-avec-pyspark-et-hadoop-sur-windows-1d17635dbcee