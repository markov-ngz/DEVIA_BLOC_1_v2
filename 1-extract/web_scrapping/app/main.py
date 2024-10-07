from html_parse import HTMLParser
from html_scrap import HTMLScrapper


class WebScrapping():

    url = "https://fr.wikiversity.org/wiki/Polonais/Vocabulaire/Se_pr%C3%A9senter"
    
    def __init__(self) -> None:
        html_scrapped = HTMLScrapper.get_content(self.url)
        raw_df_scrap = HTMLScrapper.parse_html(html_scrapped,self.url)

        print(raw_df_scrap)


