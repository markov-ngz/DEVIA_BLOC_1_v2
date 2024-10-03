"""Scrap the HTML via an Headless driver"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import requests
import logging
import os 

LOG_FILE = os.getenv("LOG_FILE")

logging.basicConfig(filename=LOG_FILE,
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def web_scrapping(url:str, driver_path:str)->str:
    """
    From a URL and the path  to the Driver that will scrap the html
    Return a str with all the html from the given page 
    """

    # driver monitor ( start / close )
    service = Service(executable_path=driver_path)
    # selenium 3
    # service=Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.headless = True
    
    # driver window instantiation
    driver = webdriver.Chrome(service=service, options=options)

    try : 
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        logger.error(str(err))
    except requests.exceptions.ConnectionError as err:
        logger.error(str(err))
    except requests.exceptions.Timeout as err:
        logger.error(str(err))
    except requests.exceptions.RequestException as err:
        logger.error(str(err))
    else:
        # browser + GET to url 
        driver.get(url)
        # "html" -> str
        html = driver.page_source
        # wait 1 seconds 
        WebDriverWait(driver, timeout=1) 
        logger.info("Successfully scrapped HTML")
        return html
    finally:
        driver.quit()