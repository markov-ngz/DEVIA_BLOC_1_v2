resource "aws_security_group" "default" {
  name        = "private"
  description = "Security Group"
  vpc_id      = aws_vpc.main.id

  tags = {
    Name = "default"
  }
}

resource "aws_vpc_security_group_ingress_rule" "default_allow_ssh_dev" {

  security_group_id = aws_security_group.default.id
  cidr_ipv4         = "${var.public_ip}/32"
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22
  description       = "Allow SSH connection"
  tags              = var.tags
}


resource "aws_vpc_security_group_egress_rule" "default_allow_ssh_dev" {

  security_group_id = aws_security_group.default.id
  cidr_ipv4         = "${var.public_ip}/32"
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22
  description       = "Allow SSH connection"
  tags              = var.tags
}

resource "aws_vpc_security_group_ingress_rule" "allow_ssh_inner" {

  security_group_id = aws_security_group.default.id
  cidr_ipv4         = "10.0.1.0/24"
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22
  description       = "Allow SSH connection"
  tags              = var.tags
}


resource "aws_vpc_security_group_egress_rule" "allow_ssh_inner" {

  security_group_id = aws_security_group.default.id
  cidr_ipv4         = "10.0.1.0/24"
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22
  description       = "Allow SSH connection"
  tags              = var.tags
}


resource "aws_vpc_security_group_egress_rule" "fix_allow_http" {
  security_group_id = aws_security_group.default.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 80
  ip_protocol       = "tcp"
  to_port           = 80
  tags              = var.tags
}

resource "aws_vpc_security_group_ingress_rule" "fix_allow_https" {

  security_group_id = aws_security_group.default.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 443
  ip_protocol       = "tcp"
  to_port           = 443
  tags              = var.tags
}


resource "aws_vpc_security_group_egress_rule" "fix_allow_https" {
  security_group_id = aws_security_group.default.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 443
  ip_protocol       = "tcp"
  to_port           = 443
  tags              = var.tags
}


resource "aws_vpc_security_group_ingress_rule" "hadoop_free" {

  security_group_id = aws_security_group.default.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 8000
  ip_protocol       = "tcp"
  to_port           = 11000
  tags              = var.tags
}


resource "aws_vpc_security_group_egress_rule" "hadoop_free" {
  security_group_id = aws_security_group.default.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 8000
  ip_protocol       = "tcp"
  to_port           = 11000
  tags              = var.tags
}