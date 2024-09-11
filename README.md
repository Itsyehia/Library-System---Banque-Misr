# DevOps Final Project
![pipeline](https://github.com/user-attachments/assets/0967f6e6-2c80-4291-81a2-261e521aa748)

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
├── Library-System---Banque-Misr/     # Main project folder containing the deployment YAML and Flask app
│   └── flask_postgres/               # Folder for Flask app integrated with PostgreSQL and Kubernetes YAMLs
│       └── deployment.yaml           # Kubernetes deployment configuration for the Flask app
│       └── service.yaml              # Kubernetes service configuration for exposing the app
│       └── pod.yaml                  # YAML file to define and manage individual Kubernetes pods
│       └── app.py                    # Main Python script for running the Flask app


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
- **Description**: Develop the web application and manage data using JSON files.

### Stage 2: Containerization
- **Tool/Technology**: Docker
- **Description**: Create a Dockerfile and containerize the Flask application for consistent deployment.

### Stage 3: Infrastructure as Code
- **Tool/Technology**: Terraform
- **Description**: Use Infrastructure as Code (IaC) to define and manage AWS resources, such as the EKS cluster and networking.

### Stage 4: Deployment
- **Tool/Technology**: Kubernetes on AWS EKS
- **Description**: Deploy and manage the Dockerized application and associated services on the AWS EKS cluster.

### Stage 5: CI/CD Integration
- **Tool/Technology**: Jenkins
- **Description**: Set up Jenkins to automate the CI/CD pipeline, including building Docker images, deploying to EKS, and running tests.

### Stage 6: Monitoring
- **Tool/Technology**: Prometheus and Grafana
- **Description**: Implement monitoring using Prometheus for metrics collection and Grafana for visualizing the health and performance of the application and infrastructure.

### Stage 7: Testing
- **Tool/Technology**: Smoke Tests
- **Description**: Perform basic tests to ensure the application is running correctly after deployment.

### Stage 8: Code Quality and Security
- **Tools/Technology**: SonarQube and Trivy
- **Description**: 
  - **SonarQube**: Analyze code quality and detect any issues or bugs.
  - **Trivy**: Scan Docker images for vulnerabilities before deployment.

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
### 6. Trivy Scan

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
                trivy image --no-progress --format json --output trivy-report.json reemwaleed/new-deployment-image:v4.0
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

### 7. Docker Build and Push

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


