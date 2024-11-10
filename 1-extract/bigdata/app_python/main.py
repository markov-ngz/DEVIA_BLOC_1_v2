from JsonLogger import JsonLogger 
from SparkHandler import SparkHandler 
from CassandraHandler import CassandraHandler 
from datetime import datetime

class Main():

    app_name : str = "bigdata"

    def __init__(self) -> None:
        """
        Execute a query from a Cassandra No-SQL database and write the data as a CSV to HDFS 
        """
        # 0. Settings 
        ## Logging 
        self.logger = JsonLogger()
        self.logger.set_logger(__name__)
        ## Cassandra settings
        columns_queried  = ["target_text" ,"target_lang" , "src_lang" , "src_text" , "created_at"]
        keyspace = 'translations' 
        table_name = 'pl_fr'
        query = 'SELECT {0} FROM {1}.{2}'.format(' , '.join(columns_queried), keyspace, table_name) 
        
        ## Hadoop Settings 
        hdfs_url = "hdfs://localhost:9000"
        file_path = "/cassandra/cassandra.csv"
        path = hdfs_url + file_path 
        # 1. Retrieve Data from Cassandra 
        cassandra = CassandraHandler()
        ## Connect to cluster
        cassandra.connect(keyspace)
        ## Configure rows of the result set returned as a tuple to easily create spark.DataFrame after 
        cassandra.set_tuple_factory() 
        ## Get the data 
        result_set  = cassandra.query(query)

        # 2. Write to HDFS 
        # Instantiate Spark Object 
        spark = SparkHandler(self.app_name)
        # Convert Result Set to pyspark DataFrame
        df = spark.session.createDataFrame(result_set, schema=columns_queried)
        # Write the dataframe to hdfs 
        spark.write(df,path,add_timestamp=True)
        
        self.logger.info("Successfully written file to {0}".format(path))
        
        
if __name__=='__main__':
    Main()
