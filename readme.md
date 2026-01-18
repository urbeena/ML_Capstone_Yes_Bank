# 📈 ML Capstone – Yes Bank Stock Price Prediction

This repository contains an **end-to-end Machine Learning pipeline** for predicting **Yes Bank stock prices** using historical data.  
The project is designed following **industry-standard ML & MLOps practices**, including modular coding, configuration-driven pipelines, logging, exception handling, and artifact management.

Each pipeline stage is implemented **step-by-step**, with:
- A config file
- A config entity
- A config artifact

This makes the project **scalable, maintainable, and production-ready**.

---

## 📂 Project Structure

ML_Capstone_Yes_Bank/
│
├── Yes_Bank/
│ ├── components/ # Core ML pipeline components
│ │ ├── data_ingestion.py
│ │ ├── data_transformation.py
│ │ ├── model_trainer.py
│ │ ├── model_evaluation.py
│ │ └── model_pusher.py
│ │
│ ├── config/ # Configuration files (YAML / constants)
│ ├── entity/ # Config & artifact entities
│ ├── exception/ # Custom exception handling
│ ├── logging/ # Centralized logging configuration
│ ├── pipeline/ # Training & prediction pipelines
│ ├── utils/ # Utility functions
│ └── init.py
│
├── data/ # Raw dataset
├── artifacts/ # Output artifacts of each pipeline stage
├── logs/ # Auto-generated log files
├── venv/ # Virtual environment (ignored in git)
│
├── main.py # Training pipeline execution
├── app.py # Prediction / deployment entry point
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md

yaml
Copy code

---

## ⚙️ Environment Setup (Step-by-Step)

### 1️⃣ Create Virtual Environment

```bash
conda create -p venv python=3.8 -y
2️⃣ Activate the Environment
bash
Copy code
conda activate venv/
3️⃣ Install Project in Editable Mode
bash
Copy code
pip install -e .
🧠 Why pip install -e .?
Installing the project in editable mode:

Makes the project importable as a package

Prevents ModuleNotFoundError

Automatically reflects code changes

Follows real-world ML/MLOps standards

🔄 Machine Learning Pipeline – Step-by-Step Implementation
✅ Step 1: Data Ingestion
Loads raw Yes Bank stock data

Splits data into training and testing sets

Saves outputs as artifacts

📁 Artifacts:

bash
Copy code
artifacts/data_ingestion/
✔ Config file created
✔ Config entity defined
✔ Data ingestion artifact generated

✅ Step 2: Data Transformation
Handles missing values

Feature engineering

Scaling and preprocessing

Saves transformed data and preprocessing object

📁 Artifacts:

bash
Copy code
artifacts/data_transformation/
✔ Config updated
✔ Transformation entity created
✔ Transformation artifacts generated

✅ Step 3: Model Trainer
Trains multiple regression models

Evaluates model performance

Selects the best-performing model

Saves trained model object

📁 Artifacts:

bash
Copy code
artifacts/model_trainer/
✔ Model trainer config implemented
✔ Model trainer entity created
✔ Trained model artifact saved