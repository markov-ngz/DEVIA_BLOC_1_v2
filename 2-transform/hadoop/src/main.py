from JsonLogger import JsonLogger
from SparkHandler import SparkHandler 
import sys 
class Main():

    app_name :str = "transformation"
    source_folders : list[str] = ["/translations/cassandra","/translations/sftp","/translations/web_scrapping"]
    delimiter :str = "\t"

    def __init__(self) -> None:
        spark = SparkHandler(self.app_name)

        spark.set_filesystem("hdfs://localhost:9000")

        for folder in self.source_folders : 
            try: 
                file_paths = spark.list_files(folder)
            except FileNotFoundError as e : 
                err = "Unable to list files from folder %s . Err : %s" % folder , str(e)
                # Log error
                continue 
            print(file_paths)
            for file_path in file_paths : 
                df = spark.session.read.option("delimiter", self.delimiter).option("header", True).csv(file_path)
                df.show(n=5)
                spark.session.stop()
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
