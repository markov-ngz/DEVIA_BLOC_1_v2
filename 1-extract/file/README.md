# File
Download a file from an SFTP server. <br>
For the SFTP server setup (terraform code & ansible ) see <b>/0-setup/sftp</b> folder of this repository
## Dockerfile
As SSH is not present (for the SFTP connection ) on default python image, a Ubuntu is used .
Please pay attention the docker-compose file :
- the private key is mounted as a volume 
- the known_hosts is mounted as a volume ( to allow ssh client connection )

## Utils
- paramiko : https://docs.paramiko.org/en/latest/api/sftp.html
