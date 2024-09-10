# DevOps Final Project

## Table of Contents
1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Why Use This Project](#why-use-this-project)
4. [Technologies Used](#technologies-used)
5. [Installation and Prerequisites](#installation-and-prerequisites)
6. [Detailed Instructions for Each Part](#detailed-instructions-for-each-part)
   - [Part 1: Application Development](#part-1-application-development)
   - [Part 2: Dockerization](#part-2-dockerization)
   - [Part 3: Infrastructure as Code with Terraform](#part-3-infrastructure-as-code-with-terraform)
   - [Part 4: Kubernetes Deployment on EKS](#part-4-kubernetes-deployment-on-eks)
   - [Part 5: CI/CD Pipeline Setup](#part-5-cicd-pipeline-setup)
   - [Part 6: Documentation and Presentation](#part-6-documentation-and-presentation)
7. [Bonus Task: Monitoring and Logging](#bonus-task-monitoring-and-logging)

---

## Project Overview
This project comprehensively integrates application development, Dockerization, Kubernetes deployment, CI/CD automation, and infrastructure management using Terraform. It allows users to apply their knowledge practically, gaining hands-on experience with real-world DevOps scenarios.

### Key Objectives:
- Develop and deploy a Python Flask application.
- Containerize the application with Docker.
- Automate infrastructure provisioning using Terraform.
- Deploy the containerized application on an AWS EKS cluster.
- Implement a CI/CD pipeline using Jenkins.
- Document the project and optionally set up monitoring and logging.

---

## Project Structure

```
Library-System---Banque-Misr/
│
├── app/                              # Directory for the Docker File 
│   └── Dockerfile                    # Defines the environment and instructions to containerize the Flask app
│
├── Documentation/                    # Contains documentation related to the project
│   └── SRS and detailed Project Documentation  # System Requirement Specification (SRS) and other docs 
│
├── Infrastructure/                   # Infrastructure configuration using Terraform
│   └── terraform/                    # Main folder for Terraform infrastructure files
│       └── Pipeline/                 # Contains Terraform scripts for setting up the CI/CD pipeline infrastructure
│       └── simple-infrastructure/    # Simple infrastructure Terraform scripts (without modules)
│       └── infrastructure-with-modules/ # Infrastructure Terraform scripts with modular setup
│
├── Pipeline/                         # Contains Jenkins pipeline scripts for CI/CD automation
│
├── Library-System---Banque-Misr/     # Main project folder containing the deployment YAML and Flask app
│   └── flask_postgres/               # Folder for Flask app integrated with PostgreSQL and Kubernetes YAMLs
│       └── deployment.yaml           # Kubernetes deployment configuration for the Flask app
│       └── service.yaml              # Kubernetes service configuration for exposing the app
│       └── pod.yaml                  # YAML file to define and manage individual Kubernetes pods
│       └── app.py                    # Main Python script for running the Flask app


```

---

## Why Use This Project

This project is designed for:
- DevOps trainees and professionals who want to gain hands-on experience in deploying applications on Kubernetes clusters.
- Developers looking to automate infrastructure provisioning using Terraform.
- Teams or individuals seeking to implement a CI/CD pipeline with Jenkins for automated deployments.

The project provides an end-to-end approach, starting from application development, Dockerization, infrastructure automation, to deployment on EKS with a fully automated CI/CD process. It is ideal for those wanting to learn or improve their DevOps skills with AWS, Kubernetes, Terraform, and Jenkins.

---

## Technologies Used
- **Python (Flask)**: For developing the web application.
- **Docker**: For containerizing the application.
- **Kubernetes**: For managing deployment on AWS EKS.
- **AWS EKS**: Managed Kubernetes service used to deploy the application.
- **Terraform**: For infrastructure as code (IaC) to provision AWS resources.
- **Jenkins**: For creating a CI/CD pipeline to automate the deployment process.
- **Prometheus & Grafana (Bonus Task)**: For monitoring and logging.

---

## Installation and Prerequisites

### Prerequisites
- **AWS Account**: You will need an AWS account to set up the EKS cluster and other services.
- **Terraform**: Install [Terraform](https://www.terraform.io/downloads.html).
- **Docker**: Install [Docker](https://docs.docker.com/get-docker/).
- **Kubernetes CLI (kubectl)**: Install [kubectl](https://kubernetes.io/docs/tasks/tools/).
- **Jenkins**: Install [Jenkins](https://www.jenkins.io/doc/book/installing/).
- **Python & Flask**: Set up Python and Flask for local development.

### Installation Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Itsyehia/Library-System---Banque-Misr.git
   cd Library-System---Banque-Misr
   ```

2. **Set up Python environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run Flask Application Locally:**
   ```bash
   python app.py
   ```

4. **Docker Setup:**
   - Build the Docker image:
     ```bash
     docker build -t your_dockerhub_username/library-json .
     ```
   - Test the Docker container:
     ```bash
     docker run -p 5000:5000 your_dockerhub_username/library-json
     ```

5. **Push Docker Image to Docker Hub:**
   ```bash
   docker login
   docker push your_dockerhub_username/library-json
   ```

6. **Terraform Setup:**
   - Go to the `EKS` folder and initialize Terraform:
     ```bash
     terraform init
     ```
   - Apply the Terraform configuration to provision the infrastructure:
     ```bash
     terraform apply
     ```

---

