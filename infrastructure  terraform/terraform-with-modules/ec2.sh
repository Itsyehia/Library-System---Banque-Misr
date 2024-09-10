#!/bin/bash

# Update all packages to the latest version
sudo yum update -y

# Install Git
sudo yum install git -y 

# Install Docker
sudo yum install docker -y

# Start Docker service
sudo service docker start

# Enable Docker to start on boot
sudo systemctl enable docker

# Download the AWS CLI version 2 installer
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# Unzip the AWS CLI installer
unzip awscliv2.zip

# Install AWS CLI version 2
sudo ./aws/install

# Download eksctl (EKS CLI) from the latest release and extract it to /tmp
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp

# Move eksctl to /usr/local/bin for global access
sudo mv /tmp/eksctl /usr/local/bin

# Download the latest version of kubectl (Kubernetes CLI)
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# Make kubectl executable
sudo chmod +x kubectl

# Move kubectl to /usr/local/bin for global access
sudo mv kubectl /usr/local/bin
