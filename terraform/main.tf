provider "aws" {
  region = "us-east-1"
}

#provider "cloudflare" {
#  email     = "adrien.laaboudi@gmail.com"
#  api_token = "43b31eb1fcb77a7e4e526f3c77b9839448211"
#}

resource "aws_instance" "packer-docker-aws" {
  ami           = "ami-0ae294107ce379ebe"
  instance_type = "t2.small"
  key_name = "deployer-key"
  tags = {
    Name = "PackerDockerAWS"
  }
}

resource "aws_key_pair" "deployer" {
  key_name = "deployer-key"
  public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILBVDW2Bqa7w6Rp+DL5rGgbhL9ERfEk+3qMhvLSG/bBt Adrien@ROG"
}

output "instance_ip" {
  description = "Public IP address for SSH access"
  value       = aws_instance.packer-docker-aws.public_ip
}