import paramiko
import pandas as pd 
import os

paramiko.util.log_to_file("paramiko.log")

ssh = paramiko.SSHClient()

key_path = os.getenv("PRIVATE_KEY_PATH")
username= os.getenv("SFTP_USERNAME")
host = os.getenv("SFTP_HOST")

remote_file_path = os.getenv("REMOTE_FILE")

key = paramiko.RSAKey.from_private_key_file(key_path)

ssh.load_system_host_keys()
ssh.connect(host, username=username, pkey=key)

with ssh.open_sftp() as sftp:
    with sftp.open(remote_file_path,"rb") as f :
        df = pd.read_csv(f,sep="\t")
        print(df)
