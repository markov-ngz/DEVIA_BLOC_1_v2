from JsonLogger import JsonLogger 
from SparkHandler import SparkHandler 
from CassandraHandler import CassandraHandler 
import os 

class Main():

    app_name : str = "bigdata"
    
    environment_variables :list[str] = ["CASSANDRA_KEYSPACE","CASSANDRA_TABLE","HDFS_URL","FILE_PATH"]

    columns_queried : list[str] = ["target_text" ,"target_lang" , "src_lang" , "src_text" , "created_at"]

    metadata : dict = {"source_type":"bigdata", "source":"cassandra"}

    def __init__(self) -> None:
        """
        Execute a query from a Cassandra No-SQL database and write the data as a CSV to HDFS 
        """
        
        # 0. Settings 
        ## Config variables
        self.load_config(self.environment_variables)
        ## Logging 
        self.logger = JsonLogger()
        self.logger.set_logger(__name__)
        ## Cassandra settings
        keyspace = self.config["CASSANDRA_KEYSPACE"]
        table_name = self.config["CASSANDRA_TABLE"]
        query = 'SELECT {0} FROM {1}.{2}'.format(' , '.join(self.columns_queried), keyspace, table_name) 
        ## Hadoop Settings 
        hdfs_url = self.config["HDFS_URL"]
        file_path = self.config["FILE_PATH"]
        path = hdfs_url + file_path 
        ## Fill metadata
        self.metadata["source"] = "{0}.{1}".format(keyspace,table_name) 
        
        # 1. Retrieve Data from Cassandra 
        cassandra = CassandraHandler()
        ## Connect to cluster
        cassandra.connect(keyspace)
        ## Configure rows of the result set returned as a tuple to easily create spark.DataFrame after 
        cassandra.set_tuple_factory() 
        ## Get the data 
        result_set  = cassandra.query(query)

        # 2. Write to HDFS 
        ## Instantiate Spark Object 
        spark = SparkHandler(self.app_name)
        ## Convert Result Set to pyspark DataFrame
        df = spark.session.createDataFrame(result_set, schema=self.columns_queried)
        ## Add source information to the Dataframe 
        df_final = spark.set_columns(df,self.metadata) 

        ## Write the dataframe to hdfs 
        spark.write(df_final,path,add_timestamp=True)
        
        self.logger.info("Successfully written file to {0}".format(path))
        
    def load_config(self, env_variables : list[str])->None : 
        self.config = {k : os.getenv(k) for k in env_variables}
        for k , v in self.config : 
            if v == None : 
                raise Exception("Environment variable %s is not set." % k ) 

if __name__=='__main__':
    Main()
