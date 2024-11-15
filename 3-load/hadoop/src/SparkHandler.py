from pyspark.sql import SparkSession , DataFrame 
from pyspark.context import SparkContext 
from pyspark.sql.functions import lit
import os 
from JsonLogger import JsonLogger 
from datetime import datetime 
from functools import reduce

class SparkHandler() : 

    app_name :str
    session : SparkSession
    context : SparkContext 

    def __init__(self, app_name:str )->None : 
        self.logger = JsonLogger()
        self.logger.set_logger(__name__)

        self.app_name = app_name 

        self.setup_env() 
        self.session = SparkSession.builder.master("local").appName(self.app_name).getOrCreate()


    def set_context(self)->None:
        self.context = SparkContext("local",self.app_name)

    def setup_env(self)->None :
        if( os.getenv("PYSPARK_PYTHON") == None ):
            os.environ["PYSPARK_PYTHON"] = "python" 
            self.logger.warning("Environment Variable PYSPARK_PYTHON not set. Setting its value as 'python'")

    def write(self,df:DataFrame, path: str , sep:str ='\t',quotechar=None,mode:str ='append', add_timestamp : bool = False)->None:
        """
        Write a DataFrame to CSV 
        """
        if add_timestamp : 
            path = self.add_timestamp(path) 
        try : 
            df.write.csv(path,quote=quotechar, sep=sep, mode=mode )
        except Exception as e : 
            self.logger.error(e)
            raise e 
    
    def read_text(self,path:str)->DataFrame:
        try:
            return self.session.read.options.text(path)
        except Exception as e :
            self.logger.error(e)
            raise e 
        
    def get_dataframes(self,folder_paths : list[str], header : bool = False , delimiter :str = ",", aggregate=False)->dict :
        """
        Read as a CSV , files present in the given folders path
        Return dict{ str <file_path> : DataFrame }  
        """
        dataframes  = {}
        for folder in folder_paths : 
            try: 
                file_paths = self.list_files(folder)
            except FileNotFoundError as e : 
                err = "Unable to list files from folder %s . Err : %s" % folder , str(e)
                self.logger.error(err)
                continue 

            for file_path in file_paths : 
                df = self.session.read.option("delimiter", delimiter).option("header", header).csv(file_path)
                dataframes[file_path] = df 
        if not aggregate : 
            return dataframes
        else : 
            return reduce(DataFrame.unionAll,dataframes)
        
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

    def set_filesystem(self, hdfs_url:str="hdfs://localhost:9000")->None:
        """
        Set a Filesystem to be used for future HDFS operations
        """
        self.URI = self.session.sparkContext._gateway.jvm.java.net.URI
        self.filesystem = self.session._jvm.org.apache.hadoop.fs.FileSystem.get(self.URI(hdfs_url),self.session._jsc.hadoopConfiguration())
    
    def list_files(self,path:str)->list[str]:
        """
        Return full HDFS path of files present from a given directory
        Example return value : ["hdfs://localhost:9000/<dir>/<filename>", ... ]
        PS : filesystem attrbiute must be set before executing this method
        """
        if("filesystem" not in self.__dir__()):
            raise AttributeError("filesystem attribute must be set before doing cluster operation. See method set_filesystem")
        
        status = self.filesystem.listStatus(self.session._jvm.org.apache.hadoop.fs.Path(path))
        # extract filename from java Object
        return [file.getPath().toString() for file in status]