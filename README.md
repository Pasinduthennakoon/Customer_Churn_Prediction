# 📊 Customer Churn Prediction System

A full-stack Machine Learning application that predicts whether a customer is likely to churn using a trained classification model. The system includes a FastAPI backend, a Streamlit frontend, and is fully containerized using Docker.

---

## 🚀 Features

- 🔍 Predict customer churn in real-time
- 📈 Displays churn probability
- 🎨 Modern Streamlit UI
- ⚡ FastAPI for high-performance inference
- 🐳 Dockerized (easy deployment)
- 🔗 Frontend ↔ Backend API integration

---

## 🧠 Machine Learning

- Model trained using customer dataset
- Encoded categorical features using saved encoders
- Outputs:
  - `churn_prediction` (0 or 1)
  - `churn_probability` (confidence score)

---

## 🏗️ Tech Stack

### Backend
- FastAPI
- Scikit-learn
- Pandas
- Pickle (model + encoder)

### Frontend
- Streamlit

### DevOps
- Docker
- Docker Compose

---

## 📂 Project Structure

```text

customer-churn-predictor/
│
├── backend/
│   ├── app.py
│   ├── encode.py
│   ├── requirements.txt
│   ├── Customer_Churn_Prediction.ipynb
│   ├── schema/
│   │   └── schema_model.py
│   └── Dockerfile
│
├── frontend/
│   ├── ui.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── .dockerignore
├── .gitignore
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Setup & Run (Docker)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/customer-churn-predictor.git
cd customer-churn-predictor
```

### 2. Run using Docker Compose
before you run docker-compose.yml. you want run Customer_Churn_Prediction.ipynb to build and save the model and encoder

```bash
docker-compose up --build
```
---

## 🌐 Access the Application

```text
Frontend (Streamlit):
http://localhost:8501
Backend API (FastAPI Docs):
http://localhost:8000/docs
```

---

## 🔌 API Endpoint

POST /predict
- Request Body
```text

{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 75.5,
  "TotalCharges": 900.5
}

```

- Response
```text

{
  "churn_prediction": 1,
  "churn_probability": 0.82
}
```

