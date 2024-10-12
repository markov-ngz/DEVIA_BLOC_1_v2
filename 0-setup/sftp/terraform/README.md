# Simple AWS instance setup

Setup of a sole instance with ports 80,443,22 opened.

## Steps

0. Be sure to be logged in to AWS or have the correct environment variables set ( see https://registry.terraform.io/providers/hashicorp/aws/latest/docs#environment-variables for detail)

1. Create Private key
```
ssh-keygen -t rsa -b 2048 -f sftp
```
2. Set value to Terraform variables : 
```
TF_VAR_public_ip = $(curl -s ifconfig.me)  # your public ip to allow only ssh from your ip 
TF_VAR_public_key_path = <path_to_your_public_key>
# Optional : 
TF_VAR_ansible_user = <ansible_ssh_user>
```
3. Launch the infrastructure
```
terraform init
terraform fmt 
terraform validate
terraform apply -auto-approve
```