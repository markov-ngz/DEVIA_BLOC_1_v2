import os 

class Settings():

    def __init__(self,
                 database_hostname:str,
                 database_port:str,
                 database_password:str,
                 database_name:str,
                 database_username: str,
                 hdfs_url :str,
                 hdfs_folder:str
                 ):
        self.database_hostname = database_hostname
        self.database_port = database_port
        self.database_password = database_password
        self.database_name = database_name
        self.database_username = database_username
        self.hdfs_url = hdfs_url
        self.hdfs_folder = hdfs_folder

settings = Settings(
    os.environ['HDFS_URL'],
    os.environ['HDFS_FOLDER'],
    os.environ['HDFS_SOURCES'],
)