# Configure the AWS provider
provider "aws" {
  region = "us-west-2"  # AWS region where resources will be created
}

# Configure the Kubernetes provider
provider "kubernetes" {
  # Endpoint URL of the EKS cluster to connect to
  host = aws_eks_cluster.main.endpoint
  
  # Authentication token for accessing the EKS cluster
  token = data.aws_eks_cluster_auth.main.token
  
  # Base64-decoded certificate authority data for the EKS cluster
  cluster_ca_certificate = base64decode(aws_eks_cluster.main.certificate_authority[0].data)
}
