terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"  # Source of the AWS provider
      version = ">= 3.0"         # Minimum version required for the AWS provider
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = var.region  # Specifies the AWS region from the variable
}
