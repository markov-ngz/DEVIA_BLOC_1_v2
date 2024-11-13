from JsonLogger import JsonLogger
from TranslationCleaner import TranslationCleaner 
from SparkHandler import SparkHandler 
import sys 
class Main():

    app_name :str = "transformation"
    source_folders : list[str] = ["/translations/cassandra","/translations/sftp","/translations/web_scrapping"]
    delimiter :str = "\t"

    def __init__(self) -> None:
        self.spark = SparkHandler(self.app_name)

        self.spark.set_filesystem("hdfs://localhost:9000")

        dataframes = self.spark.get_dataframes(self.source_folders, header=True, delimiter="\t")

        final_dataframe = TranslationCleaner().clean(dataframes)

        
        self.spark.session.stop()
        sys.exit(0)
        # for folder in self.source_folders : 
            
        #     if folder exists ? :  
        #         list files in folder 
        #     else :
        #         log error 
        #         continue 

        #     for file in files : 
        #         try : 
        #             check col format or format it , 

        #             apply transformation

        #             append it to the aggregated file 
        #         except : 
        #             log err 
        #             continue

    
if __name__=='__main__':
    Main()
