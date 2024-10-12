from html_parse import HTMLParser
from html_scrap import HTMLScrapper
import logging
import os 

class WebScrapping():

    url = "https://fr.wikiversity.org/wiki/Polonais/Vocabulaire/Se_pr%C3%A9senter"
    
    def __init__(self) -> None:
        LOG_FILE = os.getenv("LOG_FILE")
        if LOG_FILE == None:
            raise ValueError("LOG_FILE environment variable not set")

        with open(LOG_FILE,'a'):
            pass

        logging.basicConfig(filename=LOG_FILE,
                            filemode='w',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)
        logger = logging.getLogger(__name__)
        html_scrapped = HTMLScrapper.get_content(self.url)
        raw_df_scrap = HTMLParser.parse_html(html_scrapped,self.url)

        print(raw_df_scrap)


if __name__=='__main__':
    WebScrapping()
