from pyspark.sql import SparkSession , DataFrame 
from pyspark.sql.functions import lit

class SparkHandler() : 
    def __init__(self, app_name:str )->None : 
        self.session = SparkSession.builder.master("local").appName(app_name).getOrCreate()

    def write(self,df:DataFrame, path: str , format:str ='csv',mode:str ='append')->None:
        try : 
            df.write.save(path,format='csv', mode='append')
        except Exception as e : 
            raise e 
    
    def read(self,path:str)->DataFrame:
        try:
            return self.spark.read.text(path)
        except Exception as e :
            raise e 
        

    def delete(self)->None:
        pass 

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