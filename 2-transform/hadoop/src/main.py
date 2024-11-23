from JsonLogger import JsonLogger
from TranslationCleaner import TranslationCleaner 
from SparkHandler import SparkHandler 
from Settings import settings 

class Main():

    app_name :str = "transformation"
    source_folders : list[str] = settings["HDFS_SOURCES"].split("|")
    output_path : str = settings["HDFS_URL"]+settings["HDFS_FOLDER"]
    delimiter :str = "\t"

    def __init__(self) -> None:
        """
        This code does the following ; 
        1. Find Raw data files in HDFS 
        2. Clean the data & aggregate it 
        3. Write the result to HDFS 
        """

        # Setup Logger
        self.logger = JsonLogger()
        self.logger.set_logger(__name__)

        # Spark Handler and base URL 
        self.spark = SparkHandler(self.app_name)
        self.spark.set_filesystem(settings["HDFS_URL"])

        try : 
            # 1. Get raw data 
            dataframes = self.spark.get_dataframes(self.source_folders, header=True, delimiter="\t")
            self.logger.info("Found {0} DataFrames, beginning transformation ...".format(len(dataframes.keys())))

            if len(dataframes) > 0 : 
                # 2. Transform it 
                final_dataframe = TranslationCleaner().clean(dataframes)
                self.logger.info("DataFrames transformed and aggregated ".format(len(dataframes.keys())))
                
                # 3. Write output to HDFS 
                self.spark.write(final_dataframe, self.output_path + "clean.csv",add_timestamp=True)
                self.logger.info("Data Transformed. Final dataset contains {0} rows ".format(final_dataframe.count()))
                
        except Exception as e :
            self.logger.error(f"An unexpected error has occured. Error : {str(e)}")
            raise e 
        finally : 
            self.spark.session.stop()
    
if __name__=='__main__':
    Main()
