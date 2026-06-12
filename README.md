# 🚀 DevSecOps Mini Project

A complete **DevSecOps pipeline implementation** demonstrating CI/CD automation, security integration, containerization, and Kubernetes deployment.

This project showcases how to build, secure, package, scan, and deploy a containerized application using practical DevSecOps principles.

---

## 📌 Overview

This repository implements an end-to-end **DevSecOps workflow** including:

- **CI/CD automation** with GitHub Actions
- **Application containerization** using Docker
- **Security integration** across multiple stages:
  - **SAST** with Bandit
  - **SCA** with pip-audit
  - **Container scanning** with Trivy
  - **DAST** with OWASP ZAP
- **Image lifecycle management** with Docker Hub
- **Kubernetes deployment** using a local cluster created with kind
- **Automated deployment** using a self-hosted GitHub Actions runner

---

## 🧱 Architecture

```text
Git Push
   ↓
GitHub Actions (Self-hosted runner)
   ↓
Tests (pytest)
   ↓
SAST (Bandit)
   ↓
SCA (pip-audit)
   ↓
Build Docker image
   ↓
Container scan (Trivy)
   ↓
Push image to Docker Hub
   ↓
Deploy to Kubernetes (kind)
   ↓
DAST (OWASP ZAP)
```

---

## ⚙️ Technologies Used

### DevOps & CI/CD
- GitHub Actions
- Self-hosted runner (Ubuntu on WSL)
- Git with SSH authentication

### Application
- Python
- Flask
- pytest

### Containerization
- Docker
- Docker Hub

### Orchestration
- Kubernetes
- kind
- kubectl

### Security
- **Bandit** for SAST
- **pip-audit** for SCA
- **Trivy** for container vulnerability scanning
- **OWASP ZAP** for DAST

---

## 🔐 DevSecOps Pipeline

This project integrates security into the CI/CD pipeline using multiple complementary checks.

| Stage | Tool | Purpose |
|------|------|---------|
| Test | pytest | Validate application behavior |
| SAST | Bandit | Detect insecure Python code patterns |
| SCA | pip-audit | Detect vulnerable dependencies |
| Container Scan | Trivy | Detect vulnerabilities in the Docker image |
| DAST | OWASP ZAP | Test the running application from the outside |

---

## 🐳 Application

The application is a minimal Flask API exposing a simple health endpoint:

- `GET /ping` → returns `{"message": "pong!"}`

This endpoint is used in:
- unit tests
- container smoke tests
- Kubernetes health verification
- DAST scanning

---

## 🐳 Docker

### Build the application image locally

```bash
docker build -t devsecops-mini .
```

### Run the container locally

```bash
docker run -p 5000:5000 devsecops-mini
```

### Test the endpoint

```bash
curl http://localhost:5000/ping
```

---

## ☸️ Kubernetes Deployment

The application is deployed to Kubernetes using:

- `deployment.yaml`
- `service.yaml`

### Create the local Kubernetes cluster

```bash
kind create cluster --name devsecops-cluster
```

### Deploy the application

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Verify the deployment

```bash
kubectl get deployments
kubectl get pods
kubectl get svc
```

### Access the application

```bash
kubectl port-forward service/devsecops-mini-service 8080:80
curl http://localhost:8080/ping
```

---

## 🔁 CI/CD Workflow

The project includes an automated CI/CD pipeline with GitHub Actions.

### CI/CD stages

1. Run tests inside Docker
2. Run SAST with Bandit
3. Run SCA with pip-audit
4. Build the Docker image
5. Run container security scan with Trivy
6. Push the image to Docker Hub
7. Deploy the application to Kubernetes
8. Run DAST with OWASP ZAP

### Pipeline characteristics

- The workflow runs on a **self-hosted runner**
- The Docker image is automatically pushed to Docker Hub
- Kubernetes pulls the latest image and redeploys the application
- Security checks are integrated before deployment

---

## 🔐 Security Testing

### 1. SAST — Bandit

Bandit is used to perform static analysis of the Python source code.

### 2. SCA — pip-audit

pip-audit is used to detect known vulnerabilities in Python dependencies.

### 3. Container Scanning — Trivy

Trivy scans the built Docker image for OS and package vulnerabilities.

### 4. DAST — OWASP ZAP

OWASP ZAP performs dynamic security testing against the running application after deployment.

---

## 🧪 Local Development

### Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r app/requirements.txt
pip install pytest
```

### Run tests

```bash
pytest -v
```

### Run the application locally

```bash
python app/main.py
```

---

## ✅ Prerequisites

To reproduce this project locally, make sure you have:

- Python 3
- pip
- Docker
- Git
- kubectl
- kind
- GitHub account
- Docker Hub account

If you want to run the full pipeline exactly like in this project, you also need:

- A GitHub **self-hosted runner**
- Docker Hub repository secrets configured in GitHub Actions

---

## ⚙️ GitHub Actions Secrets

The pipeline requires these repository secrets:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

These are used to authenticate to Docker Hub during the image push stage.

---

## ⚙️ Self-hosted Runner

This project uses a **self-hosted GitHub Actions runner** configured on Ubuntu (WSL).

This enables the pipeline to:

- access Docker locally
- access kubectl locally
- interact with the local kind Kubernetes cluster
- deploy directly from the pipeline

---

## 🚀 How to Reproduce the Project

### 1. Clone the repository

```bash
git clone git@github.com:hasanhijazi1/devsecops-mini.git
cd devsecops-mini
```

### 2. Create the Kubernetes cluster

```bash
kind create cluster --name devsecops-cluster
```

### 3. Deploy manually (optional local test)

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl port-forward service/devsecops-mini-service 8080:80
curl http://localhost:8080/ping
```

### 4. Configure GitHub Actions secrets

Add the following repository secrets:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

### 5. Configure a self-hosted runner

Set up a GitHub Actions self-hosted runner on your Ubuntu/WSL environment.

### 6. Push code to trigger the pipeline

```bash
git add .
git commit -m "trigger pipeline"
git push
```

---

## 💡 What This Project Demonstrates

This project demonstrates practical knowledge of:

- DevSecOps pipeline design
- CI/CD automation
- containerization
- Docker image lifecycle management
- Kubernetes deployment automation
- security testing integration
- self-hosted runners
- secure software delivery practices

---

## 📈 Future Improvements

Possible next improvements include:

- Helm chart packaging
- Terraform integration
- versioned Docker image tags
- vulnerability gates based on severity
- report artifact publishing
- Kubernetes Ingress
- cloud deployment (AWS / Azure / GCP)

---

## 👤 Author

**Hassan Hijazi**  
Cybersecurity / DevSecOps Engineer

---

## ⭐ Repository Goal

This repository is intended as a hands-on demonstration of a complete **DevSecOps mini-project** combining development, automation, security, containerization, and deployment practices in a single workflow.
