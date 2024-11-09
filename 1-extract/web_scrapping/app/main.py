from html_parse import HTMLParser
from html_scrap import HTMLScrapper
from SparkHandler import SparkHandler 
import logging
import os
from sys import exit 


class WebScrapping():

    url = "https://fr.wikiversity.org/wiki/Polonais/Vocabulaire/Se_pr%C3%A9senter"
    
    hdfs_url = "hdfs://localhost:9000"

    file_path = "/web_scrapping.csv"

    def __init__(self) -> None:
        """
        Web scrapping translations pairs  :
        1. Scrap HTML from a given URL 
        2. Parse the HTML 
        3. Add metadata 
        4. Write the data to HDFS 
        """

        self.setup_logger()
        self.setup_env() 

        
        spark = SparkHandler("web-scrapping")
        try: 
            # Get HTML as str 
            html_scrapped = HTMLScrapper.get_content(self.url)
            
            # Get the translations as a DataFrame 
            raw_df_scrap = HTMLParser().get_traductions(html_scrapped,self.url, spark)
            
            # Write into HDFS 
            spark.write(raw_df_scrap,self.hdfs_url + self.file_path)
            self.logger.info("Successfully writed file to %s"  % self.file_path )

        except Exception as e : 
            self.logger.error(e)
            raise e 
        finally : 
            spark.session.stop()
    
    def setup_env(self)->None :
        if( os.getenv("PYSPARK_HOME") == None ):
            os.environ["PYSPARK_HOME"] = "python" 
    def setup_logger(self)->None:
        LOG_FILE = os.getenv("LOG_FILE")


        logging.basicConfig(filename=LOG_FILE,
                            filemode='w',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)
        
        self.logger = logging.getLogger(__name__)

        if LOG_FILE == None:
            self.logger.warning("LOG_FILE environment variable not set")
        else: 
            with open(LOG_FILE,'a'):
                self.logger.info("Logs will be written to : %s".format(LOG_FILE))


if __name__=='__main__':
    WebScrapping()
