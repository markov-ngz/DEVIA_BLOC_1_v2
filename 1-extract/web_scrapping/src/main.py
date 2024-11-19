from html_parse import HTMLParser
from html_scrap import HTMLScrapper
from SparkHandler import SparkHandler 
import logging
import os


class WebScrapping():

    url : str = "https://fr.wikiversity.org/wiki/Polonais/Vocabulaire/Se_pr%C3%A9senter" # Hard coded URL as the HTML parsing is specific to this page 

    environment_variables :list[str] = ["HDFS_URL","FILE_PATH"]

    def __init__(self) -> None:
        """
        Web scrapping translations pairs  :
        1. Scrap HTML from a given URL 
        2. Parse the HTML 
        3. Add metadata 
        4. Write the data to HDFS 
        """

        self.setup_logger()
        self.load_config(self.environment_variables) 
        
        spark = SparkHandler("web-scrapping")
        
        try: 
            # 1. Get HTML as str 
            html_scrapped = HTMLScrapper.get_content(self.url)
            
            # 2. Get the translations as a spark.DataFrame 
            raw_df_scrap = HTMLParser().get_traductions(html_scrapped,self.url, spark)
            
            # 3. Write into HDFS 
            spark.write(raw_df_scrap,self.config["HDFS_URL"] + self.config["FILE_PATH"], add_timestamp=True )
            self.logger.info("Successfully writed file to %s"  % self.file_path )

        except Exception as e : 
            self.logger.error(e)
            raise e 
        finally : 
            spark.session.stop()

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

    def load_config(self, env_variables : list[str])->None : 
        self.config = {k : os.getenv(k) for k in env_variables}
        for k , v in self.config.items() : 
            if v == None : 
                raise Exception("Environment variable %s is not set." % k ) 
            
if __name__=='__main__':
    WebScrapping()
