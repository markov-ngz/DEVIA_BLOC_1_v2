import os
from SFTPHandler import SFTPHandler
from JsonLogger import JsonLogger 
from datetime import datetime
from pyspark.sql import  DataFrame 
from  SparkHandler import SparkHandler 

class Main():

    app_name = "sftp_file"

    hdfs_url : str 

    file_path : str 

    def __init__(self) -> None:
        """
        Download a file from a SFTP server and write to HDFS  
        """
        self.logger = JsonLogger()
        self.logger.set_logger(__name__)

        # 1. Load environment variables 
        self.load_config()
        
        # 2. Instantiate SFTPHandler object 
        self.sftp  = SFTPHandler(self.key_path, self.username, self.host)
        
        # 3. Read the file and get it into a pandas Dataframe 
        # NOTE : return Bytes object instead of dataframe for more flexibility  
        df = self.sftp.read_file(self.remote_file_path)

        # 4. Create Spark Session object 
        self.spark = SparkHandler(self.app_name)

        # 5. Transform the pandas.DataFrame into  a Spark.DataFrame 
        spark_df =  self.spark.session.createDataFrame(df)

        # 6. Add metadata columns 
        df_final = self.add_columns(spark_df)

        # 7. Write the file 
        self.spark.write(df_final,self.hdfs_url + self.file_path, add_timestamp= True )

    def load_config(self):
        self.key_path = os.getenv("PRIVATE_KEY_PATH")
        self.username= os.getenv("SFTP_USERNAME")
        self.host = os.getenv("SFTP_HOST")
        self.remote_file_path = os.getenv("REMOTE_FILE")
        self.hdfs_url = os.getenv("HDFS_URL")
        self.file_path = os.getenv("FILE_PATH")

        for env in [self.key_path , self.username , self.host , self.remote_file_path, self.hdfs_url , self.file_path] :
            if env == None :
                msg = "All environment variable aren't set or could not be loaded in [PRIVATE_KEY_PATH , SFTP_USERNAME, SFTP_HOST, REMOTE_FILE], please try again."
                self.logger.error(msg) 
                raise Exception(msg)
    

    def add_columns(self, df:DataFrame)->DataFrame:
        """
        Add Hard Coded metadata information
        """
        columns  = {
                "created_at":datetime.now().strftime("%Y-%m-%d"),
                "source":"SFTP",
                "source_type":"sftp",
                "lang_origin":"french",
                "lang_target":"polish"
                }
        
        df_final = self.spark.set_columns(df, columns)

        return df_final

    
if __name__=='__main__':
    Main()

