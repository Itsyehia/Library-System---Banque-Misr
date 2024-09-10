# Fetch EKS Cluster Authentication Data
data "aws_eks_cluster_auth" "Team3" {
  # Specify the EKS cluster name to fetch authentication details
  name = aws_eks_cluster.Team3.name
}

# IAM Policy Document for EKS Full Access
data "aws_iam_policy_document" "eks_full_access" {
  statement {
    effect  = "Allow"  # Grant the specified permissions
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
    resources = ["*"]  # Apply these permissions to all resources
  }
}

# IAM Policy Document for Trusted Accounts and Users
data "aws_iam_policy_document" "trusted_account" {
  statement {
    effect  = "Allow"  # Allow the specified actions
    actions = ["sts:AssumeRole"]  # Permit role assumption

    # Allow specific users to assume the role
    principals {
      type        = "AWS"  # The principal type for role assumption
      identifiers = var.user_arns  # List of ARNs of users who can assume the role
    }
  }
}
