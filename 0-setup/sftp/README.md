# SFTP 
Setup of a SFTP server 

## Steps

1. Launch Instance ( see terraform/README for details)
```
terraform apply -auto-approve
```

2. Add user + public key (see ansible/README for details)
```
ansible-playbook playbook.yml
```
3. Upload file
```
scp -i <pr_k> <file>  <host>:~/
```

## Liens utiles
- tuto 1 : https://doc.ubuntu-fr.org/mysecureshell_sftp-server
- tuto 2 : https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server-fr


