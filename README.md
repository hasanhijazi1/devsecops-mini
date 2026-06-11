# DevSecOps Mini Project

This project demonstrates a complete DevSecOps workflow using a minimal Python Flask API. It includes testing, containerization, CI/CD automation, and security scanning.
---
## Overview

This project was created to learn and demonstrate:

- Building a basic API endpoint (/ping)
- Using Python virtual environments
- Installing and managing dependencies using pip
- Writing automated tests using pytest
- Running the application inside Docker
- Running tests inside Docker
- Configuring a full CI pipeline with GitHub Actions
- Performing Python, dependency, and container security scans
***
## Project Structure
```
devsecops-mini/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── requirements.txt
│
├── tests/
│   └── test_main.py
│
├── Dockerfile
├── Dockerfile.test
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
 ```
***
## Local Development Setup

### 1. Create project directory
```bash
mkdir devsecops-mini
cd devsecops-mini
code .
```
### 2. Create application files
```bash
mkdir app
touch app/main.py
echo "flask" > app/requirements.txt
mkdir tests
touch tests/test_main.py
touch app/__init__.py
```
### 3. Create and activate virtual environment
```bash
sudo apt install python3.12-venv -y
python3 -m venv ../venv
source ../venv/bin/activate
```
### 4. Install dependencies
```bash
pip install -r app/requirements.txt
pip install pytest
```
### 5. Run tests
```bash
pytest -v
```
If import fails: 
```bash
PYTHONPATH=. pytest -v
```
### 6. Run development server
```bash
python app/main.py
```
Server available at: http://localhost:5000/ping
***
## Docker Setup

### Dockerfile (Application)
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ app/
EXPOSE 5000
CMD ["python", "app/main.py"]
```
### Build image
```bash
docker build -t devsecops-mini .
```
### Run image
```bash
docker run -p 5000:5000 devsecops-mini
```
***
## Dockerized Test Environment

### Dockerfile.test
```dockerfile
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONPATH=/app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest
COPY app/ app/
COPY tests/ tests/
CMD ["pytest", "-v"]
```
### Build test image
docker build -f Dockerfile.test -t devsecops-mini-test .

### Run tests inside Docker
```bash
docker run devsecops-mini-test
```
***
## CI Pipeline (GitHub Actions)

This project includes a complete CI workflow that runs on every push to the main branch:
- Build test Docker image
- Run pytest inside Docker
- Run Bandit for Python security scanning
- Run pip-audit for dependency vulnerability scanning
- Build production Docker image
- Run Trivy for container vulnerability scanning

### ci.yml
```yml
name: DevSecOps CI
on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]
jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Build test image
        run: docker build -f Dockerfile.test -t devsecops-mini-test .
      - name: Run tests inside Docker
        run: docker run devsecops-mini-test

  bandit:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Install Bandit
        run: pip install bandit
      - name: Run Bandit
        run: bandit -r app

  pip-audit:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Install pip-audit
        run: pip install pip-audit
      - name: Run pip-audit
        run: pip-audit -r app/requirements.txt

  trivy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Build Docker image
        run: docker build -t devsecops-mini .
      - name: Run Trivy
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: image
          image-ref: devsecops-mini
          severity: HIGH,CRITICAL
          ignore-unfixed: true
```

## Final Result

This project demonstrates:
- Python backend development
- Unit testing with pytest
- Docker containerization
- Docker-based test execution
- CI automation with GitHub Actions
- Static code security scanning (Bandit)
- Dependency vulnerability scanning (pip-audit)
- Container vulnerability scanning (Trivy)
