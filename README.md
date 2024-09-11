
# DevOps Final Project

## Table of Contents

1. [Project Overview](#project-overview)
   - [Key Objectives](#key-objectives)
2. [Project Structure](#project-structure)
3. [Why Projects Like This Should Be Implemented](#why-projects-like-this-should-be-implemented)
4. [Stages and Technologies Used](#stages-and-technologies-used)
   - [Stage 1: Development](#stage-1-development)
   - [Stage 2: Containerization](#stage-2-containerization)
   - [Stage 3: Infrastructure as Code](#stage-3-infrastructure-as-code)
   - [Stage 4: Deployment](#stage-4-deployment)
   - [Stage 5: CI/CD Integration](#stage-5-cicd-integration)
   - [Stage 6: Testing](#stage-6-testing)
   - [Stage 7: Code Quality and Security](#stage-7-code-quality-and-security)
   - [Stage 8: Monitoring](#stage-8-monitoring)
5. [Installation and Prerequisites](#installation-and-prerequisites)
   - [Prerequisites](#prerequisites)
6. [Shared Libraries](#shared-libraries)

7. [Jenkins Pipeline](#jenkins-pipeline)
   - [1. Clean Workspace](#1-clean-workspace)
   - [2. Clone Repository](#2-clone-repository)
   - [3. SonarQube Analysis](#3-sonarqube-analysis)
   - [4. Quality Gate](#4-quality-gate)
   - [5. Docker Login](#5-docker-login)
   - [6. Trivy Scan](#6-trivy-scan)
   - [7. Docker Build and Push](#7-docker-build-and-push)
   - [8. Generate Deployment YAML](#8-generate-deployment-yaml)
   - [9. AWS Login and Configure EKS](#9-aws-login-and-configure-eks)
   - [10. Smoke Test](#10-smoke-test)
   - [11. Cleanup ](#11-cleanup-optional)
8. [References](#references)
---

## Project Overview
This project focuses on developing and deploying a Python Flask application while integrating key DevOps practices like Dockerization, Kubernetes deployment, and infrastructure automation using Terraform. It provides a practical approach to managing modern infrastructure and implementing CI/CD pipelines, allowing users to gain real-world experience with essential DevOps tools and workflows.

### Key Objectives:
- Develop and deploy a Python Flask application.
- Containerize the application with Docker.
- Automate infrastructure provisioning using Terraform.
- Deploy the containerized application on an AWS EKS cluster.
- Implement a CI/CD pipeline using Jenkins.
- Set up Prometheus and Grafana for monitoring and visualization of application performance.
- Integrate SonarQube for code quality analysis and vulnerability detection.
- Perform security scanning of Docker images using Trivy.
- Document the project and optionally configure alerts for critical conditions.

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
├── DevSecOps/                         # Contains Jenkins pipeline scripts for sonarQube and trivy only
│
├── Library-System---Banque-Misr/     # Main project folder containing the deployment YAML and Flask app
│   └── UI/                           # Folder contains the UI for the Flask app
│   └── flask_postgres/               # Folder for Flask app integrated with PostgreSQL and Kubernetes YAMLs
│       └── deployment.yaml           # Kubernetes deployment configuration for the Flask app
│       └── service.yaml              # Kubernetes service configuration for exposing the app
│       └── pod.yaml                  # YAML file to define and manage individual Kubernetes pods
│       └── app.py                    # Main Python script for running the Flask app
│
├── Note: each folder contains a seperate README.md file for further documentation

```

---

## Why Projects Like This Should Be Implemented

- Streamlined Operations: Automating infrastructure provisioning and deployments reduces overhead for operations teams, allowing them to focus on higher-value tasks.
- Enhanced Collaboration: CI/CD pipelines encourage developers, testers, and operations teams to collaborate effectively, leading to faster, more reliable releases.
- Cost Efficiency: Proper infrastructure management and monitoring can lead to cost savings by optimizing resource usage and preventing outages.
- Industry Standards: Adopting DevOps practices, containerization, and cloud-native solutions ensures that businesses remain competitive by following industry best practices for software development and deployment.

---

## Stages and Technologies Used

### Stage 1: Development
- **Tool/Technology**: Python (Flask)
- **Description**: Develop the Library management web application and manage data using JSON files.
- ![BoROOW BOOKS with One Click](https://github.com/user-attachments/assets/777e0ea4-4c78-4415-be8c-1c7e881342ea)

### Stage 2: Containerization
- **Tool/Technology**: Docker
- **Description**: Create a Dockerfile and containerize the Flask application for consistent deployment.

### Stage 3: Infrastructure as Code
- **Tool/Technology**: Terraform
- **Description**: Use Infrastructure as Code (IaC) to define and manage AWS resources, such as the EKS cluster and networking.
- ![Diagram drawio](https://github.com/user-attachments/assets/e67c8a58-6959-4157-92db-67cd78ce9355)

### Stage 4: Deployment
- **Tool/Technology**: Kubernetes on AWS EKS
- **Description**: Deploy and manage the Dockerized application and associated services on the AWS EKS cluster.

### Stage 5: CI/CD Integration
- **Tool/Technology**: Jenkins
- **Description**: Set up Jenkins to automate the CI/CD pipeline, including building Docker images, deploying to EKS, and running tests.

### Stage 6: Testing
- **Tool/Technology**: Smoke Tests
- **Description**: Perform basic tests to ensure the application is running correctly after deployment.
- ![Screenshot (929)](https://github.com/user-attachments/assets/2217d1ab-006a-416e-a9b8-78d72dc2548c)

### Stage 7: Code Quality and Security 
- **Tools/Technology**: SonarQube, Trivy, and Jenkins Credentials Manager
- **Description**: 
  - **SonarQube**: Analyze code quality and detect any issues or bugs.
  - **Jenkins Credentials Manager**: Securely manage sensitive information like SonarQube tokens, Docker credentials, and AWS access keys to ensure security in the pipeline during code quality checks and security scans.
  - **Trivy**: Scan Docker images for vulnerabilities before deployment.
  - ![Screenshot (927)](https://github.com/user-attachments/assets/2b467674-c3f0-42f1-9762-de2103d33ae3)

### Stage 8: Monitoring 
- **Tool/Technology**: Prometheus and Grafana
- **Description**: Implement monitoring using Prometheus for metrics collection and Grafana for visualizing the health and performance of the application and infrastructure.
- ![cpu usage](https://github.com/user-attachments/assets/1fa67e51-d74c-4008-87e9-3aea3970168a)
- ![conatiner network](https://github.com/user-attachments/assets/c28efdcd-bbb9-4deb-b878-09c985db5340)
---

## Installation and Prerequisites

### Prerequisites
- **AWS Account**: You will need an AWS account to set up the EKS cluster and other services.
- **Terraform**: Install [Terraform](https://www.terraform.io/downloads.html) for infrastructure provisioning.
- **Docker**: Install [Docker](https://docs.docker.com/get-docker/) for containerizing the application.
- **Kubernetes CLI (kubectl)**: Install [kubectl](https://kubernetes.io/docs/tasks/tools/) for managing Kubernetes clusters.
- **Jenkins**: Install [Jenkins](https://www.jenkins.io/doc/book/installing/) for setting up CI/CD pipelines.
- **Python & Flask**: Set up Python and Flask for developing the web application.
- **Trivy**: Install [Trivy](https://github.com/aquasecurity/trivy) for scanning Docker images for vulnerabilities.
- **SonarQube**: Set up [SonarQube](https://www.sonarqube.org/downloads/) for code quality and security analysis.
- **Prometheus & Grafana**: Install [Prometheus](https://prometheus.io/docs/prometheus/latest/installation/) and [Grafana](https://grafana.com/docs/grafana/latest/installation/) for monitoring and logging.


---
## Shared Libraries 

This section explains the shared library functions used in the Jenkins pipeline later on . Ensure your Jenkins environment is configured with the necessary credentials before using these functions.
![shared lin](https://github.com/user-attachments/assets/f387038f-0a15-4e18-b94d-40c1f5e43913)

### `dockerOperations.groovy` - Functions

---

### 1. **BuildAndPush**

**Code:**
```groovy
def BuildAndPush(String repoDir, String imageTag) {
    dir(repoDir) {
        if (isUnix()) {
            sh "docker build -t reemwaleed/new-deploymentnew-image:${imageTag} ."
            sh "docker push reemwaleed/new-deploymentnew-image:${imageTag}"
            sh "docker rmi -f reemwaleed/new-deploymentnew-image:${imageTag}"
        } else {
            bat "docker build -t reemwaleed/new-deploymentnew-image:${imageTag} ."
            bat "docker push reemwaleed/new-deploymentnew-image:${imageTag}"
            bat "docker rmi -f reemwaleed/new-deploymentnew-image:${imageTag}"
        }
    }
}
```
**Explanation:**  
Builds a Docker image from the specified directory, pushes it to a Docker registry, and removes the local image.

**Parameters:**
- `repoDir`: Directory containing the Dockerfile.
- `imageTag`: Tag for the Docker image.

**Usage:**
```groovy
dockerOperations.BuildAndPush('path/to/repo', 'v1.0.0')
```
---

### 2. **generateDeploymentYAML**

**Code:**
```groovy
def generateDeploymentYAML(imageTag, filePath) {
    sh """
    cat <<EOF > ${filePath}/deployment.yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: library-json-deployment
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: library-json
      template:
        metadata:
          labels:
            app: library-json
        spec:
          containers:
            name: library-json-container
            image: reemwaleed/new-deployment-image:${imageTag}
  EOF"""
}

```
**Explanation:**  
Generates a Kubernetes deployment YAML with the updetaed Docker image tag.

**Parameters:**
- `imageTag`: Docker image tag.
- `filePath`: Path to save the YAML file.

**Usage:**
```groovy
dockerOperations.generateDeploymentYAML('v1.0.0', 'path/to/yaml')
```


---
## Jenkins Pipeline

![pipeline](https://github.com/user-attachments/assets/56ac4333-7fd4-4b52-b1c2-289e0a11e563)


---
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

### 7. Trivy Scan

**Code:**

```groovy
stage('Trivy Scan') {
    steps {
        script {
            // Install the latest version of Trivy CLI
            sh '''
                curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- latest
            '''

            // Run Trivy scan and save the report in JSON format
            sh '''
                trivy image --no-progress --format json --output trivy-report.json reemwaleed/new-deployment-image:v${DOCKER_IMAGE_TAG}
            '''

            // Archive the Trivy report as an artifact
            archiveArtifacts artifacts: 'trivy-report.json', allowEmptyArchive: true
        }
    }
}
```

**Explanation:**

This stage performs a security vulnerability scan using **Trivy** on the Docker image to ensure it's free of known security issues before deployment. **Trivy**, scans the Docker image, then saves the scan report in a JSON file. The report is then archived in Jenkins for future review.

---


### 8. Generate Deployment YAML

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

### 9. AWS Login and Configure EKS

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

### 10. Smoke Test

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

### 11. Cleanup 
**Code:**

```groovy
stage('Cleanup') {
    steps {
        script {
            // Optionally clean up resources such as Docker images
            sh 'docker rmi ${DOCKER_IMAGE_TAG} || true'
        }
    }
}
```
Explanation:
This stage  is used to clean up resources such as old Docker images after a successful deployment. This helps in freeing up space and maintaining a clean environment.



---

## References

- **Terraform Modules**: [GitHub Repository](https://github.com/7hundredtech/EKS-Terraform--Project/tree/main/EKS_Project/modules)
- **Bonus Resource**: [Kubernetes Monitoring Setup](https://www.coachdevops.com/2022/05/how-to-setup-monitoring-on-kubernetes.html)
- **Trivy**: [Issue Discussion](https://github.com/aquasecurity/trivy/issues/3660)
- **Shared Library Tutorial**: [YouTube Video](https://www.youtube.com/watch?v=RvY5b--wnE0)
- **Shared Libraries Repository**: [Shared Libraries Repo](https://github.com/reemsarhan/sharedLibsRepo)

---


