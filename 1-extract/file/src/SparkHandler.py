from pyspark.sql import SparkSession , DataFrame 
from pyspark.sql.functions import lit
import os 
from JsonLogger import JsonLogger 

class SparkHandler() : 
    def __init__(self, app_name:str )->None : 
        self.logger = JsonLogger()
        self.logger.set_logger(__name__)

        self.setup_env() 
        self.session = SparkSession.builder.master("local").appName(app_name).getOrCreate()

    def setup_env(self)->None :
        if( os.getenv("PYSPARK_HOME") == None ):
            os.environ["PYSPARK_HOME"] = "python" 
            self.logger.warning("Environment Variable PYSPARK_HOME not set. Setting its value as 'python'")

    def write(self,df:DataFrame, path: str , format:str ='csv',mode:str ='append')->None:
        try : 
            df.write.save(path,format=format, mode=mode)
        except Exception as e : 
            self.logger.error(e)
            raise e 
    
    def read(self,path:str)->DataFrame:
        try:
            return self.session.read.text(path)
        except Exception as e :
            self.logger.error(e)
            raise e 

    def set_columns(self, df : DataFrame , col : dict )-> DataFrame:
        """
        Args :
         df : pyspark.sql.DataFrame
         col : dict{str <col_name> :  str <value> }
        Return pyspark.sql.DataFrame 
        """
        for  k , v  in col.items() : 
            df = df.withColumn(k ,lit(v) )
        return df 