import os 

LOG_FILE = os.getenv("LOG_FILE")
if LOG_FILE == None:
    raise ValueError("LOG_FILE environment variable not set")

with open(LOG_FILE,'a'):
    pass

import html_parse
import scrap

import logging

logging.basicConfig(filename=LOG_FILE,
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


DRIVER_PATH=os.getenv("DRIVER_PATH")
if DRIVER_PATH == None:
    msg = "DRIVER_PATH environment variable not set"
    logger.error(msg)
    raise ValueError(msg)

url_scrapped = "https://fr.wikiversity.org/wiki/Polonais/Vocabulaire/Se_pr%C3%A9senter"

def main()->None:
    try:
        html_scrapped = scrap.web_scrapping(url_scrapped,DRIVER_PATH)
        raw_df_scrap = html_parse.parse_html(html_scrapped,url_scrapped)
        logger.info("Successfully parsed the HTML")
    except Exception as e :
        logger.error(f"Unexpected error occured : {str(e)}")
    

if __name__=='__main__':
    main()