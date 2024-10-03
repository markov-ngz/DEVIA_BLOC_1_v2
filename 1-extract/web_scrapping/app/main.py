import html_parse
import scrap

url_scrapped = "https://fr.wikiversity.org/wiki/Polonais/Vocabulaire/Se_pr%C3%A9senter"

html_scrapped = scrap.web_scrapping(url_scrapped,"utils/msedgedriver.exe")
raw_df_scrap = html_parse.parse_html(html_scrapped,url_scrapped)

print(raw_df_scrap)