from html_parse import HTMLParser
from html_scrap import HTMLScrapper
from SparkHandler import SparkHandler 
import logging
import os 

class WebScrapping():

    url = "https://fr.wikiversity.org/wiki/Polonais/Vocabulaire/Se_pr%C3%A9senter"
    
    def __init__(self) -> None:

        self.setup_logger()
        # html_scrapped = HTMLScrapper.get_content(self.url)
        # raw_df_scrap = HTMLParser.parse_html(html_scrapped,self.url)
        #print(raw_df_scrap)


        spark = SparkHandler("web-scrapping")

        df = spark.read("hdfs://127.0.0.1:9000/hello.csv") 

        df.show() 
    
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
