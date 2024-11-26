variable "tags" {
  type        = map(string)
  description = "resource's tag"
}

variable "public_ip" {
  type      = string
  sensitive = true
}

variable "ami_id" {
  type = string
}

variable "instance_type" {
  type        = string
  description = "Aws type of instance"
  default     = "t2.micro"
}

variable "key_name" {
  type = string
}

variable "ec2_public_key" {
  type        = string
  sensitive   = true
  description = "public key path"
}

variable "ec2_default_user" {
  type    = string
  default = "ubuntu"
}