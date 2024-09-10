resource "aws_eks_cluster" "cluster-1" {
  name     = var.cluster_name
  role_arn = var.eks_role_arn

  vpc_config {
    subnet_ids = [var.default_az1_id,var.default_az2_id]
  }

  depends_on = [
    var.eks-AmazonEKSClusterPolicy_arn, 
    var.eks-AmazonEKSVPCResourceController_arn,
  ]
}

resource "aws_eks_node_group" "worker_node_group" {
  cluster_name    = var.cluster_name
  node_group_name = "team-3-tf-worker_node_group"
  node_role_arn   = var.eks-node-group-role_arn
  subnet_ids      = [var.default_az1_id,var.default_az2_id]
  
 

  scaling_config {
    desired_size = 1
    max_size     = 1
    min_size     = 1
  }
  
  update_config {
    max_unavailable = 1
  }

  depends_on = [
    var.AmazonEKSWorkerNodePolicy_arn,
    var.AmazonEKS_CNI_Policy_arn,
    var.AmazonEC2ContainerRegistryReadOnly_arn,
  ]
}