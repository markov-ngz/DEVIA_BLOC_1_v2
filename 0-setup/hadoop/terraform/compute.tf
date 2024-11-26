resource "aws_instance" "default" {

  ami                         = var.ami_id
  instance_type               = var.instance_type
  key_name                    = aws_key_pair.main.key_name
  subnet_id                   = aws_subnet.public.id
  security_groups             = [aws_security_group.default.id]
  associate_public_ip_address = true
  availability_zone           = "eu-west-3a"
  private_ip                  = "10.0.1.4" # aws subnet reserves 4 first ip address
  user_data                   = "name=default"

  root_block_device {
    volume_size = 10
  }
  tags = {
    Name = "namenode"
  }
  depends_on = [aws_security_group.default]
}

resource "aws_instance" "datanode" {

  ami                         = var.ami_id
  instance_type               = var.instance_type
  key_name                    = aws_key_pair.main.key_name
  subnet_id                   = aws_subnet.public.id
  security_groups             = [aws_security_group.default.id]
  associate_public_ip_address = true
  availability_zone           = "eu-west-3a"
  private_ip                  = "10.0.1.5" # aws subnet reserves 4 first ip address
  user_data                   = "name=default"

  root_block_device {
    volume_size = 10
  }
  tags = {
    Name = "datanode"
  }
  depends_on = [aws_security_group.default]
}