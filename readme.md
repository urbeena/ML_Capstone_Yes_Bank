## 📈 ML Capstone – Yes Bank Stock Price Prediction

This project implements an **end-to-end Machine Learning pipeline** to predict **Yes Bank stock prices** using historical market data.
It follows **industry-standard project structuring**, **modular design**, **logging**, **exception handling**, and **MLOps-ready pipelines**.

---

## 🚀 Project Highlights

* End-to-end ML lifecycle: ingestion → transformation → training → evaluation → deployment
* Clean, modular, production-ready folder structure
* Centralized logging & custom exception handling
* YAML-based configuration management
* Streamlit app for real-time predictions

---

## 📂 Project Structure

```
ML_Capstone_Yes_Bank/
│
├── Yes_Bank/
│   ├── components/
│   ├── config/
│   ├── entity/
│   ├── exception/
│   ├── logging/
│   ├── pipeline/
│   ├── utils/
│   └── __init__.py
│
├── data/
├── artifacts/
├── logs/
├── main.py
├── app.py
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

---

## 📁 Folder-wise Documentation

---

## 1️⃣ `Yes_Bank/components/`

Contains the **core ML logic**, each module handling one stage of the pipeline.

| File                     | Description                                    |
| ------------------------ | ---------------------------------------------- |
| `data_ingestion.py`      | Loads raw dataset and splits into train/test   |
| `data_transformation.py` | Feature engineering, scaling, preprocessing    |
| `model_trainer.py`       | Trains multiple ML models and selects best one |
|                          | Evaluates trained model using metrics          |
|                          | Pushes the final model for deployment          |

---

## 2️⃣ `Yes_Bank/config/`

Configuration-driven pipeline setup.



---

## 3️⃣ `Yes_Bank/entity/`

Defines **dataclasses** for configuration and artifact tracking.

| File                            | Description                       |
| ------------------------------- | --------------------------------- |
| `data_ingestion_entity.py`      | Ingestion config & artifacts      |
| `data_transformation_entity.py` | Transformation config & artifacts |
| `model_trainer_entity.py`       | Model training config             |
|                                 | Evaluation results                |

✔️ Enables clean data flow between pipeline stages

---

## 4️⃣ `Yes_Bank/exception/`

Centralized custom exception handling.

| File           | Description                                  |
| -------------- | -------------------------------------------- |
| `exception.py` | CustomException class with traceback support |

---

## 5️⃣ `Yes_Bank/logging/`

Project-wide logging setup.

| File        | Description                             |
| ----------- | --------------------------------------- |
| `logger.py` | Logger configuration and log formatting |

📌 Logs stored automatically in `/logs`

---

## 6️⃣ `Yes_Bank/pipeline/`

Orchestrates ML workflows.

| File                     | Description                       |
| ------------------------ | --------------------------------- |
| `training_pipeline.py`   | Runs full training pipeline       |
| `prediction_pipeline.py` | Loads model and makes predictions |

---

## 7️⃣ `Yes_Bank/utils/`

Helper functions and reusable logic.

| File            | Description                         |
| --------------- | ----------------------------------- |
| `main_utils.py` | Common utility functions            |
| `ml_utils.py`   | Prediction & model helper utilities |

---

## 8️⃣ `data/`

Contains the raw dataset.

| File           | Description                    |
| -------------- | ------------------------------ |
| `yes_bank.csv` | Historical Yes Bank stock data |

---

## 9️⃣ `artifacts/`

Stores outputs from each pipeline stage.

```
artifacts/
├── data_ingestion/
├── data_transformation/
├── model_trainer/
└── model_evaluation/
```

✔️ Makes pipeline reproducible & debuggable

---

## 🔟 `logs/`

Auto-generated logs for debugging & monitoring.

---

## 📌 Root Files

| File               | Purpose                           |
| ------------------ | --------------------------------- |
| `main.py`          | Entry point for training pipeline |
| `app.py`           | Streamlit app for prediction      |
| `requirements.txt` | Project dependencies              |
| `setup.py`         | Package setup for deployment      |
| `.gitignore`       | Git ignored files                 |

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
ENVIRONMENT SETUP (ALREADY IMPLEMENTED)

Step 1: Create virtual environment

conda create -p venv python=3.8 -y

Step 2: Activate virtual environment

conda activate venv/

Step 3: Install dependencies

pip install -r requirements.txt

Step 4: Install project in editable mode

pip install -e .

Why pip install -e . ?

• Makes the project importable as a package
• Prevents ModuleNotFoundError
• Automatically reflects code changes
• Follows real-world ML/MLOps standards```

### 2️⃣ Train the Model

```bash
python main.py
```

### 3️⃣ Run Prediction App

```bash
streamlit run app.py
```

---

## 📊 ML Workflow

```
Data Ingestion → Data Transformation → Model Training → Model Evaluation → Deployment
```



## ✨ Author

**Urbeena Rashid**
ML Capstone Project

---

⭐ If you like this project, don’t forget to star the repository!
