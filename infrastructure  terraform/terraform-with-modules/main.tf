# To deploy VPC
module "vpc" {
  source       = "./modules/vpc"
  region       = var.region
  project_name = var.project_name
}
# To deploy Securtiy Group
module "securitygroup" {
  source = "./modules/securitygroup"
  vpc_id = module.vpc.vpc_id
}
# To deploy IAM Roles and Permissions
module "IAM_Roles" {
  source = "./modules/IAM_Roles"
}
# To deploy EKS Cluster and EKS Worker Node Group
module "eks" {
  source                                 = "./modules/eks"
  cluster_name                           = var.cluster_name
  eks_role_arn                           = module.IAM_Roles.eks_role_arn
  eks-node-group-role_arn                = module.IAM_Roles.eks-node-group-role_arn
  default_az1_id                         = module.vpc.default_az1_id
  default_az2_id                         = module.vpc.default_az2_id
  eks-AmazonEKSClusterPolicy_arn         = module.IAM_Roles.eks-AmazonEKSClusterPolicy_arn
  eks-AmazonEKSVPCResourceController_arn = module.IAM_Roles.eks-AmazonEKSVPCResourceController_arn
  AmazonEKSWorkerNodePolicy_arn          = module.IAM_Roles.AmazonEKSWorkerNodePolicy_arn
  AmazonEKS_CNI_Policy_arn               = module.IAM_Roles.AmazonEKS_CNI_Policy_arn
  AmazonEC2ContainerRegistryReadOnly_arn = module.IAM_Roles.AmazonEC2ContainerRegistryReadOnly_arn
}
# To deploy EC2 instance ( K8-Client Server)
module "ec2" {
  source                    = "./modules/ec2"
  instance_type             = var.instance_type
  key_name                  = var.key_name
  ami                       = var.ami
  iam_instance_profile_name = module.IAM_Roles.iam_instance_profile_name
  ec2_security_group_id     = module.securitygroup.ec2_security_group_id
}