from pyspark.sql import SparkSession , DataFrame 
from abc import ABC

class SparkHandler() : 
    def __init__(self, app_name:str , )->None : 
        self.spark = SparkSession.builder.appName(app_name).getOrCreate()

    def write(self)->None:
        pass 
    
    def read(self,path:str)->DataFrame:
        try:
            return self.spark.read.text(path)
        except Exception as e :
            raise e 
        

    def delete(self)->None:
        pass 