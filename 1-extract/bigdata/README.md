# Request to a Big Data System

## Bug encountered 
Please note that this was first tried to be done with Java . <br>
However the following bug could not be resolved : 
```
21/11/02 18:02:35 INFO BlockManagerMasterEndpoint: BlockManagerMasterEndpoint up Exception in thread "main" java.lang.IllegalAccessError: class org.apache.spark.storage.StorageUtils$ (in unnamed module @0x34e9fd99) cannot access class sun.nio.ch.DirectBuffer (in module java.base) because module java.base does not export sun.nio.ch to unnamed module @0x34e9fd99 at org.apache.spark.storage.StorageUtils$.
```
The following was added to maven-compile plugin : 
```
<configuration>
    <compilerArgs>
        <arg>--add-opens</arg>
        <arg>java.management/sun.management=ALL-UNNAMED</arg>
    </compilerArgs>
</configuration> 
```
But it might just as well be a Java version compatibility problem ?  <br>
see: https://stackoverflow.com/questions/69814385/exception-in-thread-main-java-lang-illegalaccesserror-class-org-apache-spark 
## Liens utiles
- https://docs.datastax.com/en/developer/java-driver/4.0/manual/core/index.html
- https://stackoverflow.com/questions/21956042/mapping-a-jdbc-resultset-to-an-object ( mapping resultset to a list of object)