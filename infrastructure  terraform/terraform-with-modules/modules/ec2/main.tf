# use data source to get a registered amazon linux 2 ami
data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "owner-alias"
    values = ["amazon"]
  }

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm*"]
  }
}

# launch the ec2 instance
resource "aws_instance" "ec2_instance" {
  ami                         = var.ami
  instance_type               = var.instance_type
  key_name                    = var.key_name
  vpc_security_group_ids      = [var.ec2_security_group_id]
  user_data                   = file("./ec2.sh")
  associate_public_ip_address = true
  iam_instance_profile        = var.iam_instance_profile_name

  tags = {
    Name = "team-3-tf-k8-client-vm"

  }

}
