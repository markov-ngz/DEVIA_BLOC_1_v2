from JsonLogger import JsonLogger
from SparkHandler import SparkHandler 

class Main():

    app_name :str = "transformation"
    source_folders : list[str] = ["/cassandra","/sftp","/web_scrapping"]

    def __init__(self) -> None:
        spark = SparkHandler(self.app_name)

        spark.set_filesystem("hdfs://localhost:9000")

        for folder in self.source_folders : 
            file_paths = spark.list_files(folder)
            for file_path in file_paths : 
                print(file_path)

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
