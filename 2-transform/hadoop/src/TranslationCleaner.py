from pyspark.sql import DataFrame

class TranslationCleaner():

    def __init__(self) -> None:
        pass

    def clean(self,dfs:list[DataFrame])->DataFrame:
        """
        Clean the given spark.DataFrames and then Aggregate it 
        """
        pass 

    def clean_quotechar(self,df:DataFrame)->DataFrame:
        pass 
    def clean_unwanted_characters(self, df:DataFrame)->DataFrame :  
        pass
    