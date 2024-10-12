# SFTP 
Setup of a SFTP server 

## Steps

1. Launch Instance ( see terraform/README for details)

2. Add instance public ip to list of known hosts
```
ssh-keyscan -H $AWS_INSTANCE_IP >> ~/.ssh/known_hosts 
```
2. Update ansible/inventory.yml file
```
default:
    ansible_host: <host>
    ansible_user: <sftp_user>
```
2. Set the following environment variables 
```
export SFTP_USER=<sftp_user>
export SFTP_PUBLIC_KEY=<public_key_path>
```
2. Add user + public key (see ansible/README for details)
```
ansible-playbook -i inventory.yml --keyfile <path_private_key> playbook.yml
```
3. Upload file
```
scp -i <pr_k> <file>  <sftp_user>@<host>:~/
```

## Liens utiles
- tuto 1 : https://doc.ubuntu-fr.org/mysecureshell_sftp-server


