# Fetch EKS Cluster Auth
data "aws_eks_cluster_auth" "Team3" {
  name = aws_eks_cluster.Team3.name
}

data "aws_iam_policy_document" "eks_full_access" {
  statement {
    effect  = "Allow"
    actions = [
      "eks:DescribeCluster",
      "eks:ListClusters",
      "eks:ListNodegroups",
      "eks:ListFargateProfiles",
      "eks:ListUpdates",
      "eks:DescribeNodegroup",
      "eks:DescribeFargateProfile",
      "eks:DescribeUpdate",
      "eks:UpdateNodegroupConfig",
      "eks:UpdateNodegroupVersion",
      "eks:CreateNodegroup",
      "eks:CreateFargateProfile",
      "eks:DeleteNodegroup",
      "eks:DeleteFargateProfile",
      "eks:TagResource",
      "eks:UntagResource"
    ]
    resources = ["*"]
  }
}


# IAM Policy Document for Trusted Account and Users
data "aws_iam_policy_document" "trusted_account" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]

    # Allow specific users to assume the role
    principals {
      type        = "AWS"
      identifiers = var.user_arns
    }
  }
}
