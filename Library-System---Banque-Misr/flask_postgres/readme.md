# Library System Setup

This project is a library system built with Flask, providing two roles: user and admin. Users can borrow and return books, register and log in, search for books, and browse the entire collection. Admins can log in, manage the collection of books, and view users.

## Flask Application Overview

### User Role:
- **Borrow and Return Books**: Users can borrow multiple books at a time and return them.
- **Register and Login**: New users can register for an account and log in to the system.
- **Search and Browse Books**: Users can search for specific books by title or author and view the entire library collection.

### Admin Role:
- **Login**: Admins can log in to manage the library.
- **Manage Books**: Admins have the ability to add or remove books from the collection.
- **View Users and Books**: Admins can browse the list of registered users and view all books available in the library.

---

## Project Setup and Commands

### Docker Commands

#### Building, Pushing, and Pulling Docker Images

To manage the Docker images for the project, use the following commands:

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

---

### Kubernetes Commands

#### Managing Kubernetes Resources

To manage the Kubernetes resources, use the following commands:

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

3. **Access Running Services in Minikube**:

    To access the running services in Minikube, use the following command:

    ```bash
    minikube service library-json-service
    ```

---

## Running the Flask App

Once your resources are deployed, the Flask app will provide two interfaces: one for users and one for admins. Both roles have separate functions, with users able to borrow and return books, while admins manage the library’s inventory.

---
