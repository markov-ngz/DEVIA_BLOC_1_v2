# Troubleshoot
Reference : https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html 

## Commands
List Files in a given directory
```
hadoop fs -ls /<dir>
```
Copy a file 
```
hdfs dfs -put <file> /path/<file>
```
List block devices
```
lsblk
```
Get Informations about a file 
```
hdfs fsck /user/hello.txt -files -blocks -locations
```