# AWS Infrastructure Setup
 ![Diagram drawio](https://github.com/user-attachments/assets/e67c8a58-6959-4157-92db-67cd78ce9355)
This directory contains resources and pipelines to create and manage AWS infrastructure using Terraform. It is organized into three main components: `pipeline`, `simple-Infrastructure`, and `terraform-with-modules`.

## Folder Structure

### 1. **pipeline**
This folder contains a basic infrastructure pipeline script for provisioning resources on AWS.

- **infrastructure pipeline.txt**: Outlines the steps for deploying the infrastructure via the pipeline.

### 2. **simple-Infrastructure**
This folder contains the necessary Terraform configuration files to create a simple AWS infrastructure setup.

- **data.tf**: Defines data sources for retrieving information about existing AWS resources.
- **eks.tf**: Manages AWS EKS (Elastic Kubernetes Service) cluster deployment.
- **iam.tf**: Manages IAM roles and policies for the infrastructure.
- **main.tf**: The entry point for Terraform configuration, linking various components.
- **networking.tf**: Defines the VPC, subnets, and other networking components.
- **temp.tf**: Temporary or experimental Terraform configurations.
- **variables.tf**: Defines the input variables used across the Terraform configurations.

### 3. **terraform-with-modules**
This folder contains reusable Terraform modules to organize the infrastructure's components.

#### Modules:
- **IAM_Roles**: Manages IAM roles and policies.
- **ec2**: Manages EC2 instances.
- **eks**: Manages EKS clusters.
- **securitygroup**: Manages security groups for EC2 and EKS.
- **vpc**: Defines the VPC, subnets, and routing tables.

#### Additional Files:
- **ec2.sh**: Shell script for managing EC2 instances.
- **main.tf**: Main configuration file to invoke the modules and deploy infrastructure.
- **output.tf**: Defines outputs for important resources like EC2 IP addresses, cluster details, etc.
- **terraform.tf**: Backend configuration for state management.
- **terraform.tfvars**: Specifies values for the input variables.
- **variable.tf**: Contains all variables used in the main configuration.

## How to Use

1. **Pipeline Deployment**: Follow the steps in `infrastructure pipeline.txt` to deploy the AWS infrastructure via the jenkins pipeline.
2. **Simple Infrastructure Setup**: Navigate to `simple-Infrastructure` and run the standard Terraform workflow:
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```
3. **Modular Infrastructure**: Navigate to `terraform-with-modules`, and use the pre-built modules for more complex deployments. Follow the same Terraform workflow as above.

## Notes
- Ensure you have valid AWS credentials set up before deploying.
- Review and modify the variables in `terraform.tfvars` as needed for your environment.

---
