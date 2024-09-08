# Create EKS Cluster
resource "aws_eks_cluster" "Team3" {
  name     = "Team3-cluster"
  role_arn  = aws_iam_role.eks.arn

  vpc_config {
    subnet_ids = [
      aws_subnet.team3_first_subnet.id,
      aws_subnet.team3_second_subnet.id,
    ]
    security_group_ids = [aws_security_group.eks.id]
  }

  depends_on = [
    aws_iam_role_policy_attachment.eks_policy
  ]
}

# Create EKS Node Group
resource "aws_eks_node_group" "Team3" {
  cluster_name    = aws_eks_cluster.Team3.name
  node_group_name = "Team3-node-group"
  node_role_arn   = aws_iam_role.eks_node_group.arn
  subnet_ids       = [
    aws_subnet.team3_first_subnet.id,
    aws_subnet.team3_second_subnet.id,
  ]
  scaling_config {
    desired_size = 2
    max_size     = 2
    min_size     = 2
  }
}
