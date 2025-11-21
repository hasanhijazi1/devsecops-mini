# DevSecOps Mini Project — Summary + Commands

## ✔️ What We Built
A minimal Flask API to learn DevSecOps fundamentals:
- What an API endpoint is (`/ping`)
- Using a virtual environment (venv)
- Installing Python dependencies with `pip`
- Writing automated tests using `pytest`
- Using Flask’s test client to test endpoints without running the server
- Preparing the project for Docker, CI/CD, and security scans

---

## ✔️ Project Structure
```
devsecops-mini/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── requirements.txt
│
└── tests/
    └── test_main.py
```

---

## ✔️ All Commands Used (In Order)

### 🔧 Create project
mkdir devsecops-mini
cd devsecops-mini
code .

### 📁 Create project files
mkdir app
touch app/main.py
echo "flask" > app/requirements.txt
mkdir tests
touch tests/test_main.py
touch app/__init__.py

### 🐍 Virtual environment setup
sudo apt install python3.12-venv -y
python3 -m venv ../venv
source ../venv/bin/activate

### 📦 Install Python dependencies
pip install -r app/requirements.txt
pip install pytest

### 🧪 Run tests
pytest -v
# If imports fail:
PYTHONPATH=. pytest -v

### ▶️ Run the server
python app/main.py

To stop:
CTRL + C

---

## ✔️ What You Learned (Short Summary)
- `/ping` is an API endpoint (a URL that returns JSON)
- Virtual environments isolate dependencies
- `pip` installs Python libraries, `apt` installs system tools
- Automated tests validate API behavior without running the server

---

## ✔️ Next Steps
- Create Dockerfile  
- Build Docker image  
- Run container  
- Add CI/CD workflow (GitHub Actions)  
- Add security scanning (Bandit, pip-audit, Trivy)

