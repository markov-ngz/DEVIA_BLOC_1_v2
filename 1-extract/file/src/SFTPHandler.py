import paramiko
import pandas as pd 
from JsonLogger import JsonLogger 

class SFTPHandler():

    def __init__(self, key_path:str, username:str, host:str) -> None:
        
        self.logger = JsonLogger()
        self.logger.set_logger(__name__)

        paramiko.util.log_to_file("paramiko.log")

        self.key_path = key_path
        self.username= username
        self.host = host 

        self.key = paramiko.RSAKey.from_private_key_file(self.key_path)
        
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()

    def read_file(self, remote_file_path:str, sep: str="\t")->pd.DataFrame :   
        """
        Instantiate a the connection and retrieve the file bytes 
        """
        try : 
            with self.ssh.open_sftp() as sftp:
                with sftp.open(remote_file_path,"rb") as f :
                    df = pd.read_csv(f,sep=sep)
            self.logger({"method":"read_file","result":"success","file":remote_file_path})
            return df 
        except Exception as e :
            self.logger.error({"method":"read_file","result":"failure","file":remote_file_path,"error":str(e)})
            raise e  