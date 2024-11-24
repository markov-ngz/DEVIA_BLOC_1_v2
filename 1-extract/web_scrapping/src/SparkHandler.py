from pyspark.sql import SparkSession , DataFrame 
from pyspark.sql.functions import lit
import os 
from JsonLogger import JsonLogger 
from datetime import datetime 

class SparkHandler() : 
    def __init__(self, app_name:str )->None : 
        self.logger = JsonLogger()
        self.logger.set_logger(__name__)

        self.setup_env() 
        self.session = SparkSession.builder.config("spark.hadoop.dfs.client.use.datanode.hostname","true").master("local[*]").appName(app_name).getOrCreate()

    def setup_env(self)->None :
        if( os.getenv("PYSPARK_PYTHON") == None ):
            os.environ["PYSPARK_PYTHON"] = "python" 
            self.logger.warning("Environment Variable PYSPARK_PYTHON not set. Setting its value as 'python'")

    def write(self,df:DataFrame, path: str , sep:str ='\t',quotechar=None,mode:str ='append', add_timestamp : bool = False, header=None)->None:
        if add_timestamp : 
            path = self.add_timestamp(path) 
        
        try : 
            df.write.csv(path,quote=quotechar, sep=sep, mode=mode, header=header )
        except Exception as e : 
            self.logger.error(str(e))
            raise e 
    
    def read(self,path:str)->DataFrame:
        try:
            return self.session.read.text(path)
        except Exception as e :
            self.logger.error(str(e))
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
    
    def add_timestamp(self, path:str, format="%Y%m%d")->str :
        """
        Prefix the name of the file with a timestamp of the given format  
        """
        now : str  = datetime.now().strftime(format)
        split : list  = path.split("/")
        split[-1] = now +"_"+split[-1]

        return '/'.join(split)
