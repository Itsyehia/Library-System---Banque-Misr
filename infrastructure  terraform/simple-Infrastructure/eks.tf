# Create EKS Cluster
resource "aws_eks_cluster" "Team3" {
  name     = "Team3-cluster"  # Name of the EKS cluster
  role_arn  = aws_iam_role.eks.arn  # ARN of the IAM role used by the EKS cluster

  vpc_config {
    subnet_ids = [
      aws_subnet.team3_first_subnet.id,  # IDs of the subnets for the cluster
      aws_subnet.team3_second_subnet.id,
    ]
    security_group_ids = [aws_security_group.eks.id]  # Security group IDs associated with the cluster
  }

  # Ensure the EKS cluster is created only after the IAM role policy attachment is applied
  depends_on = [
    aws_iam_role_policy_attachment.eks_policy
  ]
}

# Create EKS Node Group
resource "aws_eks_node_group" "Team3" {
  cluster_name    = aws_eks_cluster.Team3.name  # Name of the EKS cluster to associate with the node group
  node_group_name = "Team3-node-group"  # Name of the EKS node group
  node_role_arn   = aws_iam_role.eks_node_group.arn  # ARN of the IAM role for the node group
  subnet_ids       = [
    aws_subnet.team3_first_subnet.id,  # IDs of the subnets where the nodes will be launched
    aws_subnet.team3_second_subnet.id,
  ]
  scaling_config {
    desired_size = 2  # Desired number of nodes in the node group
    max_size     = 2  # Maximum number of nodes in the node group
    min_size     = 2  # Minimum number of nodes in the node group
  }
}
