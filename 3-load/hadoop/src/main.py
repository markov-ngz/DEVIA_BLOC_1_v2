from JsonLogger import JsonLogger
from SparkHandler import SparkHandler 
from Settings import settings


class Main():
    def __init__(self) -> None:

        self.logger = JsonLogger()
        self.logger.set_logger(__name__)

if __name__ == "__main__":
    Main()