from pyspark.sql import SparkSession
from abc import ABC

class SparkHandler() : 
    def __init__(self, app_name:str , )->None : 
        self.spark = SparkSession.builder.appName(app_name).getOrCreate()

    def write(self)->None:
        pass 
    
    def read(self)->None:
        pass

    def delete(self)->None:
        pass 