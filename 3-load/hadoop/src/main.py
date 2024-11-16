from JsonLogger import JsonLogger
from SparkHandler import SparkHandler 
from Settings import settings
from TranslationLoader import TranslationLoader
from pyspark.sql import Row

class Main():

    app_name : str =  "hadoop_load"

    def __init__(self) -> None:
        """
        
        """
        self.logger = JsonLogger()
        self.logger.set_logger(__name__)

        # 1. Get clean data 
        spark = SparkHandler(self.app_name)
        spark.set_filesystem()
        df = spark.get_dataframes([settings.hdfs_folder],header=True,delimiter="\t", aggregate=True)

        # 2. Get langues and sources 
        distinct_langs : list[Row] = df.select('lang_origin','lang_target').distinct().collect()
        distinct_source : list[Row] = df.select('source_columns','source_type').distinct().collect()

        loader = TranslationLoader(settings.database_hostname, settings.database_port,settings.database_name ,settings.database_username, settings.database_password)


if __name__ == "__main__":
    Main()