import os 

class Settings():

    def __init__(self,
                 hdfs_url :str,
                 hdfs_folder:str,
                 hdfs_sources:str
                 ):
        self.hdfs_url = hdfs_url
        self.hdfs_folder = hdfs_folder
        self.hdfs_sources = hdfs_sources

settings = Settings(
    os.environ['HDFS_URL'],
    os.environ['HDFS_FOLDER'],
    os.environ['HDFS_SOURCES'],
)