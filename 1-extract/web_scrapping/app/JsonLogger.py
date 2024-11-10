import logging 
from logging import Logger
import os 
import json

class JsonLogger():
    """
    Custom Logger to write message formatted as JSON 
    """
    
    LOG_FILE = os.getenv("LOG_FILE")
    
    def __init__(self) -> None:

        self.setup_logger() 

    def setup_logger(self)->None:

        logging.basicConfig(filename=self.LOG_FILE,
                            filemode='w',
                            format='{"time":"%(asctime)s","name":"%(name)s","level":"%(levelname)s","data":%(message)s}',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)
        
        
        self.logger = logging.getLogger(__name__) 
        
        if self.LOG_FILE == None:
            self.logger.warning("LOG_FILE environment variable not set")
        else: 
            with open(self.LOG_FILE,'a'):
                self.logger.info("Logs will be written to : {0}".format(self.LOG_FILE))

    def set_logger(self, name:str)->None: 
        self.logger = logging.getLogger(name)
    def warning(self, data:dict)->None:
        self.logger.warning(self.to_json(data))
    def error(self, data:dict)->None:
        self.logger.error(self.to_json(data)) 
    def debug(self, data:dict)->None:
        self.logger.debug(self.to_json(data)) 
    def info(self, data:dict)->None: 
        self.logger.info(self.to_json(data)) 
    def to_json(self,data: str|dict)->str:
        """
        Convert to JSON if the data passed is a dict otherwise build a dict 
        """
        try: 
            return json.dumps(data) if type(data)!= str else json.dumps({"message":data})
        except Exception as e : 
            raise  e