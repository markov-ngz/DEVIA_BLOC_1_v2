# Bug
- YARN can only see 1 node ( datanode or namenode idk )
- Can create folder but unable to create a file or read file from outside the cluster ( can't  read from within ? )
Trace when writing 
```
2024-11-04 13:56:20 2024-11-04 12:56:20 INFO  StateChange:802 - BLOCK* allocate blk_1073741825_1001, replicas=172.20.0.5:9866 for /user/data/test.txt

2024-11-04 13:56:41 2024-11-04 12:56:41 INFO  BlockPlacementPolicy:912 - Not enough replicas was chosen. Reason: {NO_REQUIRED_STORAGE_TYPE=1}

2024-11-04 13:56:41 2024-11-04 12:56:41 INFO  BlockPlacementPolicy:912 - Not enough replicas was chosen. Reason: {NO_REQUIRED_STORAGE_TYPE=1}

2024-11-04 13:56:41 2024-11-04 12:56:41 WARN  BlockPlacementPolicy:489 - Failed to place enough replicas, still in need of 1 to reach 1 (unavailableStorages=[], storagePolicy=BlockStoragePolicy{HOT:7, storageTypes=[DISK], creationFallbacks=[], replicationFallbacks=[ARCHIVE]}, newBlock=true) For more information, please enable DEBUG log level on org.apache.hadoop.hdfs.server.blockmanagement.BlockPlacementPolicy and org.apache.hadoop.net.NetworkTopology

2024-11-04 13:56:41 2024-11-04 12:56:41 WARN  BlockStoragePolicy:161 - Failed to place enough replicas: expected size is 1 but only 0 storage types can be selected (replication=1, selected=[], unavailable=[DISK], removed=[DISK], policy=BlockStoragePolicy{HOT:7, storageTypes=[DISK], creationFallbacks=[], replicationFallbacks=[ARCHIVE]})

2024-11-04 13:56:41 2024-11-04 12:56:41 WARN  BlockPlacementPolicy:489 - Failed to place enough replicas, still in need of 1 to reach 1 (unavailableStorages=[DISK], storagePolicy=BlockStoragePolicy{HOT:7, storageTypes=[DISK], creationFallbacks=[], replicationFallbacks=[ARCHIVE]}, newBlock=true) All required storage types are unavailable:  unavailableStorages=[DISK], storagePolicy=BlockStoragePolicy{HOT:7, storageTypes=[DISK], creationFallbacks=[], replicationFallbacks=[ARCHIVE]}

2024-11-04 13:56:41 2024-11-04 12:56:41 INFO  Server:3087 - IPC Server handler 2 on default port 8020, call Call#5 Retry#0 org.apache.hadoop.hdfs.protocol.ClientProtocol.addBlock from 172.20.0.1:45870
2024-11-04 13:56:41 java.io.IOException: File /user/data/test.txt could only be written to 0 of the 1 minReplication nodes. There are 1 datanode(s) running and 1 node(s) are excluded in this operation.
```

Trace when trying to read ( java errror, namenode just retires and datanode does not get anything)
```
org.apache.hadoop.hdfs.BlockMissingException: Could not obtain block: BP-2125719915-172.20.0.4-1730724959863:blk_1073741826_1002 file=/user/hello.txt No live nodes contain current block Block locations: DatanodeInfoWithStorage[172.20.0.5:9866,DS-cddcb631-da9e-4119-8c0e-3957234bfb63,DISK] Dead nodes:  DatanodeInfoWithStorage[172.20.0.5:9866,DS-cddcb631-da9e-4119-8c0e-3957234bfb63,DISK]
```
Also can't download UI but can see ofc the metadata

==> connectibity issues 