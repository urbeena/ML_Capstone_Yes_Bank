# ML Capstone – Yes Bank Stock Price Prediction 📈

This repository contains the initial setup and project structure for the **Yes Bank Stock Price Prediction** machine learning capstone project.  
The project follows **industry-standard Python packaging, logging, and exception handling practices**.

---

## 📂 Project Structure

ML_Capstone_Yes_Bank/
│
├── Yes_Bank/
│   ├── exception/        # Custom exception handling
│   ├── logging/          # Centralized logging configuration
│   ├── __init__.py
│
├── data/                 # Dataset directory
├── logs/                 # Auto-generated log files
├── venv/                 # Virtual environment (ignored in git)
│
├── data_loader.py        # Data loading logic
├── requirements.txt      # Project dependencies
├── setup.py              # Package configuration
├── .gitignore
└── readme.md

---

## ⚙️ Environment Setup

### 1️⃣ Create Virtual Environment

conda create -p venv python==3.8 -y

---

### 2️⃣ Activate the Environment

conda activate venv/

---

### 3️⃣ Install Project in Editable Mode

pip install -e .

---

## 🧠 Why `pip install -e .`?

Installing the project in editable mode:
- Makes the project importable as a package
- Avoids module import errors
- Reflects code changes instantly
- Follows real-world ML/MLOps standards

---

## 🚧 Current Status

✔ Project structure implemented  
✔ Logging system configured  
✔ Custom exception handling added  
✔ Package installation enabled  



---

## 👩‍💻 Author

Urbeena Rashid  
Machine Learning & Data Science Enthusiast  

---

⚠️ Note:  
The virtual environment (`venv/`) is excluded from version control.  
Always recreate the environment using the steps above.

