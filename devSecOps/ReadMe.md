# DevSecOps Pipeline

This folder contains the configuration for integrating **SonarQube** and **Trivy** into your Jenkins pipeline for code quality and security checks.

## Pipeline Stages

### 1. SonarQube Analysis
Performs static code analysis to identify bugs, vulnerabilities, and code smells.

#### Steps:
1. Configure SonarQube Scanner in Jenkins.
2. Use Jenkins credentials to fetch the SonarQube token.
3. Run the SonarQube scanner:

   - **For Unix**:
     ```bash
     ${scannerHome}/bin/sonar-scanner \
       -Dsonar.projectKey=LibrarySystem \
       -Dsonar.sources=./Library-System---Banque-Misr \
       -Dsonar.login=${SONAR_TOKEN}
     ```
   - **For Windows**:
     ```cmd
     ${scannerHome}\\bin\\sonar-scanner ^
       -Dsonar.projectKey=LibrarySystem ^
       -Dsonar.sources=./Library-System---Banque-Misr ^
       -Dsonar.login=${SONAR_TOKEN}
     ```

4. Wait for SonarQube's **Quality Gate** result to determine if the pipeline should proceed or fail.

### 2. Trivy Scan
Scans Docker images for vulnerabilities.

#### Steps:
1. Install the latest version of Trivy:
   ```bash
   curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- latest
