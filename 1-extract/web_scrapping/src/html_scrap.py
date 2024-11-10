# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.wait import WebDriverWait
import requests


class HTMLScrapper():
        
    @staticmethod
    def get_content(url:str)->str:
        """
        Make a GET request to the URL and give the 
        """
        try:
            response = requests.get(url)
            if response.status_code != 200:
                # log the status code retunred 
                raise requests.HTTPError("Expected status code to be 200. Got instead %s".format(response.status_code))
            return response.content
        except Exception as e: 
            # log the error
            raise e
        
    
    # def selenium_scrapping(url:str, driver_path:str)->str:
    #     """
    #     From a URL and the path  to the Driver that will scrap the html
    #     Return a str with all the html from the given page 
    #     """

    #     # driver monitor ( start / close )
    #     service = Service(executable_path=driver_path)

    #     options = webdriver.EdgeOptions()
    #     options.add_argument("--headless=new")
        
    #     # driver window instantiation
    #     driver = webdriver.Edge(service=service, options=options)



    #     try : 
    #         r = requests.get(url)
    #         r.raise_for_status()
    #     except requests.exceptions.HTTPError as errh:
    #         print ("Http Error:",errh)
    #     except requests.exceptions.ConnectionError as errc:
    #         print ("Error Connecting:",errc)
    #     except requests.exceptions.Timeout as errt:
    #         print ("Timeout Error:",errt)
    #     except requests.exceptions.RequestException as err:
    #         print ("Bad request:",err)
    #     else:
    #         # browser + GET to url 
    #         driver.get(url)
    #         # "html" -> str
    #         html = driver.page_source
    #         # wait 1 seconds 
    #         WebDriverWait(driver, timeout=1) 

    #         return html
    #     finally:
    #         driver.quit()