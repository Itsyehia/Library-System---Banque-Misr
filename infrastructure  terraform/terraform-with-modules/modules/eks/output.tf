output "eks_cluster_name" {
  value = aws_eks_cluster.cluster-1.name
}

output "eks_cluster_arn" {
  value = aws_eks_cluster.cluster-1.arn
}

output "eks_cluster_id" {
  value = aws_eks_cluster.cluster-1.id
}

output "eks_node_group_arn" {
  value = aws_eks_node_group.worker_node_group.arn
}

output "eks_node_group_name" {
  value = aws_eks_node_group.worker_node_group.node_group_name
}

output "eks_node_group_id" {
  value = aws_eks_node_group.worker_node_group.id
}

