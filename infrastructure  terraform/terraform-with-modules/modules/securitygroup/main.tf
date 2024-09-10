
# create security group for the K8-EC2Client-VM
resource "aws_security_group" "ec2_security_group" {
  name        = "team-3-k8-client-VM_sg"
  description = "allow ssh on ports  22"
  vpc_id      = var.vpc_id

   ingress {
    description = "ssh access"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "team-3-tf-k8-client-VM_sg"
  }
}