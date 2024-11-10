"""Parse the HTML"""
from bs4 import BeautifulSoup
from datetime import datetime
from pyspark.sql import  DataFrame 
from SparkHandler import SparkHandler
import os 
import logging

LOG_FILE = os.getenv("LOG_FILE")

logging.basicConfig(filename=LOG_FILE,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class HTMLParser():

                    
    def get_traductions(self, html:str,from_url:str, spark: SparkHandler , lang_origin:str = "french" , lang_target:str="polish")->DataFrame:
        """
        Parse the html of the specific url : 
        "https://fr.wikiversity.org/wiki/Polonais/Vocabulaire/Se_pr%C3%A9senter"
        
        """
        # 1. Parse HTML 
        language_list = self.parse_html(html)
        
        # 2. Transform into a Spark.DataFrame 
        df = spark.session.createDataFrame(language_list,schema = ["text_origin","text_target"])
        
        # Add additionnal information 
        columns  = {
                "created_at":datetime.now().strftime("%Y-%m-%d"),
                "source":from_url,
                "source_type":"scrapping",
                "lang_origin":lang_origin,
                "lang_target":lang_target
                }
        
        df_final = spark.set_columns(df, columns)

        
        return df_final
    
    def parse_html(self, html:str)->list:
                # container 
        language_list = []

        # html soup to parse
        soup  =  BeautifulSoup(html, 'html.parser')

        tables = soup.find_all("table")

        for table in tables:
            if "polonais" not in table.tbody.find_all("tr")[0].text :
                continue
            rows = table.tbody.find_all("tr")
            for row in rows[1:]: # no header
                tds = row.find_all("td")
                if len(tds) == 2:
                    pl_text = tds[0].text
                    fr_text = tds[1].text
                    pair = [pl_text, fr_text]
                    language_list.append(pair)

        return language_list 