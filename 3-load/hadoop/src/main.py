from JsonLogger import JsonLogger
from SparkHandler import SparkHandler 
from Settings import settings


class Main():

    app_name : str =  "hadoop_load"

    def __init__(self) -> None:
        """
        
        """
        self.logger = JsonLogger()
        self.logger.set_logger(__name__)

        # 1. Get clean data 
        spark = SparkHandler(self.app_name)
        spark.set_context()
        df = spark.get_dataframes([settings.hdfs_folder],header=True,delimiter="\t", aggregate=True)

    
        



if __name__ == "__main__":
    Main()