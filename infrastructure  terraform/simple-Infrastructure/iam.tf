# Create a security group for the EKS cluster
resource "aws_security_group" "eks" {
  vpc_id = aws_vpc.Team3.id  # ID of the VPC to associate with the security group

  # Ingress rule to allow HTTPS traffic
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Allow traffic from any IP address
  }

  # Ingress rule to allow HTTP traffic
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Allow traffic from any IP address
  }

  # Ingress rule to allow traffic on port 5173 (commonly used for development servers)
  ingress {
    from_port   = 5173
    to_port     = 5173
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Allow traffic from any IP address
  }

  # Ingress rule to allow traffic on port 30000 (commonly used for NodePort services in Kubernetes)
  ingress {
    from_port   = 30000
    to_port     = 30000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Allow traffic from any IP address
  }

  # Egress rule to allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"  # -1 means all protocols
    cidr_blocks = ["0.0.0.0/0"]  # Allow outbound traffic to any IP address
  }

  tags = {
    Name = "eks-sg"  # Tag to identify the security group
  }
}

# Create an IAM role for the EKS cluster
resource "aws_iam_role" "eks" {
  name = "eks-cluster-role-team1"  # Name of the IAM role

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action    = "sts:AssumeRole"
        Effect    = "Allow"
        Principal = {
          Service = "eks.amazonaws.com"  # EKS service that can assume this role
        }
      }
    ]
  })
}

# Attach the Amazon EKS cluster policy to the IAM role
resource "aws_iam_role_policy_attachment" "eks_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"  # Policy ARN for EKS cluster
  role     = aws_iam_role.eks.name  # IAM role to attach the policy to
}

# Create an IAM role for the EKS Node Group
resource "aws_iam_role" "eks_node_group" {
  name = "eks-node-group-role"  # Name of the IAM role

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action    = "sts:AssumeRole"
        Effect    = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"  # EC2 service that can assume this role
        }
      }
    ]
  })
}

# Attach the Amazon EKS worker node policy to the IAM role
resource "aws_iam_role_policy_attachment" "eks_node_group_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"  # Policy ARN for EKS worker nodes
  role     = aws_iam_role.eks_node_group.name  # IAM role to attach the policy to
}

# Attach the Amazon EC2 Container Registry (ECR) read-only policy to the IAM role
resource "aws_iam_role_policy_attachment" "eks_node_group_ecr" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"  # Policy ARN for ECR read-only access
  role     = aws_iam_role.eks_node_group.name  # IAM role to attach the policy to
}

# Attach the Amazon EKS CNI policy to the IAM role
resource "aws_iam_role_policy_attachment" "eks_node_group_cni" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"  # Policy ARN for EKS CNI
  role     = aws_iam_role.eks_node_group.name  # IAM role to attach the policy to
}

# Create an IAM role for master access
resource "aws_iam_role" "master_access_team_3" {
  name               = "masterPermissionRole"  # Name of the IAM role
  assume_role_policy = data.aws_iam_policy_document.trusted_account.json  # Policy document for role assumption
  tags               = var.tags  # Tags to apply to the IAM role
}

# Attach the master access policy to the IAM role
resource "aws_iam_role_policy" "master_access_policy" {
  name   = "masterAccessPolicy"  # Name of the policy
  role   = aws_iam_role.master_access_team_3.id  # IAM role to attach the policy to
  policy = data.aws_iam_policy_document.eks_full_access.json  # Policy document for full EKS access
}
