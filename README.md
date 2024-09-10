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


---
## Jenkins Pipeline

### 1. Clean Workspace

**Code:**

```groovy
stage('Clean Workspace') {
    steps {
        script {
            deleteDir() // Deletes the entire workspace
        }
    }
}
```

**Explanation:**  
This stage removes all files and directories from the workspace to avoid issues with old or conflicting files then starts with a clean slate.

---

### 2. Clone Repository

**Code:**

```groovy
stage('Clone Repository') {
    steps {
        script {
            if (isUnix()) {
                sh 'git clone https://github.com/Itsyehia/Library-System---Banque-Misr.git'
            } else {
                bat 'git clone https://github.com/Itsyehia/Library-System---Banque-Misr.git'
            }
        }
    }
}
```

**Explanation:**  
This stage clones the project repository from GitHub into the Jenkins workspace. It ensures that the latest code and configuration files are available for the build and deployment processes.

---

### 3. SonarQube Analysis

**Code:**

```groovy
stage('SonarQube Analysis') {
    environment {
        scannerHome = tool 'SonarQubeScanner' // Name of SonarQube scanner tool in Jenkins
    }
    steps {
        withSonarQubeEnv('SonarQube') { // Use the SonarQube environment configured in Jenkins
            script {
                withCredentials([string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN')]) {
                    if (isUnix()) {
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=LibrarySystem -Dsonar.sources=./Library-System---Banque-Misr -Dsonar.login=${SONAR_TOKEN}"
                    } else {
                        bat "${scannerHome}\\bin\\sonar-scanner -Dsonar.projectKey=LibrarySystem -Dsonar.sources=./Library-System---Banque-Misr -Dsonar.login=${SONAR_TOKEN}"
                    }
                }
            }
        }
    }
}
```

**Explanation:**  
This stage runs a SonarQube analysis to check the code quality and identify any issues such as bugs, vulnerabilities, or code smells. It helps ensure that the code meets quality standards before proceeding further.

---

### 4. Quality Gate

**Code:**

```groovy
stage('Quality Gate') {
    steps {
        timeout(time: 1, unit: 'MINUTES') {
            waitForQualityGate abortPipeline: true // Ensures the pipeline waits for the SonarQube quality gate result
        }
    }
}
```

**Explanation:**  
This stage waits for SonarQube to finish its analysis and provides feedback on code quality. If the quality gate fails (indicating issues in the code), the pipeline will be aborted to prevent deploying problematic code.

---

### 5. Docker Login

**Code:**

```groovy
stage('Docker Login') {
    steps {
        script {
            withCredentials([usernamePassword(credentialsId: 'docker_account', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                sh '''
                    docker logout || true
                    echo ${DOCKER_PASSWORD} | docker login ${DOCKER_REGISTRY} -u ${DOCKER_USERNAME} --password-stdin
                '''
            }
        }
    }
}
```

**Explanation:**  
This stage logs into Docker Hub using the provided credentials. It ensures that Jenkins can push Docker images to the Docker registry, which is necessary for deploying the application.

---

### 6. Docker Build and Push

**Code:**

```groovy
stage('Docker Build and Push') {
    steps {
        script {
               // build and push docker image with a groovy fucntion created separately 
              dockerOperations.BuildAndPush('Library-System---Banque-Misr/app', "${DOCKER_IMAGE_TAG}")
        }
    }
}
```

**Explanation:**  
This stage builds a Docker image from the application code and then pushes it to Docker Hub. The Docker image contains the application and all its dependencies, making it portable and easy to deploy.

---

### 7. Generate Deployment YAML

**Code:**

```groovy
stage('Generate Deployment YAML') {
    steps {
        script {
            // Generate a deployment YAML file with the new image
            def filePath = 'Library-System---Banque-Misr/Library-System---Banque-Misr/flask_postgres'
            dockerOperations.generateDeploymentYAML("${DOCKER_IMAGE_TAG}", filePath)
        }
    }
}
```

**Explanation:**  
This stage generates a Kubernetes deployment YAML file with the updated Docker image tag. This YAML file defines how the application should be deployed on Kubernetes.

---

### 8. AWS Login and Configure EKS

**Code:**

```groovy
stage('AWS Login and Configure EKS') {
    steps {
        script {
            withCredentials([aws(credentialsId: 'aws_credentials', accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
               // get current user credentials to ensure login 
                sh 'aws sts get-caller-identity'
                sh "aws eks update-kubeconfig --region us-west-2 --name Team3-cluster"

               // apply Yaml files
                dir('Library-System---Banque-Misr/Library-System---Banque-Misr/flask_postgres') {
                    sh '''
                        kubectl apply -f pod.yaml
                        kubectl apply -f deployment.yaml
                        kubectl apply -f service.yaml
                        kubectl get svc
                    '''
                }
            }
        }
    }
}
```

**Explanation:**  
This stage logs into AWS and configures access to the EKS cluster.ensure that your local kubectl tool is correctly configured to communicate with the EKS cluster, enabling you to perform operations and manage Kubernetes resources on AWS. .It then applies the Kubernetes configuration files to deploy the application on the cluster and verifies the services are running.

---

### 9. Smoke Test

**Code:**

```groovy
stage('Smoke Test') {
    steps {
        script {
            withCredentials([aws(credentialsId: 'aws_credentials', accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                def lb_dns = ""
                def retries = 5
                def delay = 30 // seconds

                lb_dns = sh(script: "kubectl get svc library-json-service -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'", returnStdout: true).trim()

                retry(retries) {
                    echo "Testing server at http://${lb_dns}/landing"
                    def response = sh(script: "curl -s -o /dev/null -w \"%{http_code}\" http://${lb_dns}/landing", returnStdout: true).trim()
                    if (response != "200") {
                        error "Server not ready. Response code: ${response}"
                    } else {
                        echo "Server is running"
                    }
                }
            }
        }
    }
}
```

**Explanation:**  
This stage performs a smoke test to ensure that the application is running correctly. It checks if the application responds with a `200 OK` status code from a specific endpoint. If the server isn’t ready, it retries the test several times.

---


