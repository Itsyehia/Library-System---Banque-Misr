# Project Setup and Commands without using pipeline

## Docker Commands

### Building, Pushing, and Pulling Docker Images

To manage Docker images, use the following commands:

1. **Build the Docker Image**:

    ```bash
    docker build -t reemwaleed/python:bm-project-v10 .
    docker build -t reemwaleed/library_json:latest .
    ```

2. **Push the Docker Image to Docker Hub**:

    ```bash
    docker push reemwaleed/python:bm-project-v10
    docker push reemwaleed/library_json:latest
    ```

3. **Pull the Docker Image from Docker Hub**:

    ```bash
    docker pull reemwaleed/python:bm-project-v10
    docker pull reemwaleed/library_json:latest
    ```

## Kubernetes Commands

### Managing Kubernetes Resources

To manage your Kubernetes resources, use these commands:

1. **Delete Existing Resources**:

    ```bash
    kubectl delete -f deployment.yaml
    kubectl delete -f persistent-volume.yaml
    kubectl delete -f persistent-volume-claim.yaml
    kubectl delete -f pod.yaml
    kubectl delete -f service.yaml
    ```

2. **Apply New Configuration**:

    ```bash
    kubectl apply -f persistent-volume-claim.yaml
    kubectl apply -f persistent-volume.yaml
    kubectl apply -f pod.yaml
    kubectl apply -f service.yaml
    kubectl apply -f deployment.yaml
    ```

## Running Services

To access the running services in Minikube, use the following command:

```bash
minikube service library-json-service
