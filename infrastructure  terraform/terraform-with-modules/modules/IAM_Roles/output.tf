output "ec2_role_arn" {
  value = aws_iam_role.ec2_role.arn
}

output "ec2_role_id" {
  value = aws_iam_role.ec2_role.id
}

output "ec2_role_name" {
  value = aws_iam_role.ec2_role.name
}

output "iam_instance_profile_name" {
  value = aws_iam_instance_profile.ec2_instance_profile.name
}

output "eks_role_arn" {
  value = aws_iam_role.eks_role.arn
}
output "eks_role_id" {
  value = aws_iam_role.eks_role.id
}
output "eks_role_name" {
  value = aws_iam_role.eks_role.name
}

output "eks-node-group-role_arn" {
  value = aws_iam_role.eks-node-group-role.arn
}

output "eks-node-group-role_id" {
  value = aws_iam_role.eks-node-group-role.id
}

output "eks-node-group-role_name" {
  value = aws_iam_role.eks-node-group-role.name
}

output "eks_node_grouAmazonEKSWorkerNodePolicy_arn" {
  value = aws_iam_role_policy_attachment.AmazonEKSWorkerNodePolicy.policy_arn
}


output "eks-AmazonEKSClusterPolicy_arn" {
  value = aws_iam_role_policy_attachment.eks-AmazonEKSClusterPolicy.policy_arn
}


output "eks-AmazonEKSVPCResourceController_arn" {
  value = aws_iam_role_policy_attachment.eks-AmazonEKSVPCResourceController.policy_arn
}

output "AmazonEKSWorkerNodePolicy_arn" {
  value = aws_iam_role_policy_attachment.AmazonEKSWorkerNodePolicy.policy_arn
}

output "AmazonEKS_CNI_Policy_arn" {
  value = aws_iam_role_policy_attachment.AmazonEKS_CNI_Policy.policy_arn
}

output "AmazonEC2ContainerRegistryReadOnly_arn" {
  value = aws_iam_role_policy_attachment.AmazonEC2ContainerRegistryReadOnly.policy_arn
}