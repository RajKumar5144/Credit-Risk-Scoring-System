# 💳 Credit Risk Scoring System (ML Web App)

An end-to-end **Credit Risk Scoring Application** that predicts the probability of loan default using Machine Learning and deploys the model as a **web application** using **FastAPI** (backend) and **Streamlit** (frontend).

---

## 🚀 Project Overview

Financial institutions need to assess whether a loan applicant is likely to default.  
This project builds a **data-driven credit risk scoring system** that:

- Predicts **probability of default**
- Generates a **risk score (0–1000)**
- Classifies applicants into **Low / Medium / High Risk**
- Provides an automated **loan decision** (Approve / Manual Review / Reject)

---

## 🧠 Machine Learning Approach

- **Model Used**: LightGBM Classifier  
- **Target Variable**: `loan_status`  
  - `0` → Non-default  
  - `1` → Default  

### 📊 Model Performance
- **AUC-ROC**: ~0.94  
- **KS Statistic**: ~74  
- **Class Imbalance Handling**: SMOTE  

---

## 🏗️ Architecture

User (Browser)
|
| (inputs)
v
Streamlit UI ───────────────▶ FastAPI Backend
|
| (ML inference)
v
Trained LightGBM Model
|
v
Risk Score & Decision
---

## 🗂️ Project Structure

credit-risk-prod/
│
├── app.py # FastAPI backend (ML inference API)
├── ui.py # Streamlit frontend (Web UI)
├── requirements.txt # Python dependencies
├── .gitignore # Ignored files (data, models, cache)
└── README.md # Project documentation
---

## ⚙️ Tech Stack

- **Python**
- **Pandas / NumPy**
- **Scikit-learn**
- **LightGBM**
- **FastAPI**
- **Uvicorn**
- **Streamlit**
- **Matplotlib / Seaborn**
- **Git & GitHub**

---

## 🌐 Web Application Features

### 1️⃣ Applicant Risk Prediction
- Input applicant details
- Get:
  - Probability of default
  - Risk score
  - Risk band
  - Loan decision

### 2️⃣ Portfolio Risk Dashboard
- Histogram of predicted risk scores
- Model performance metrics (AUC & KS)
- Business insight charts
- Fairness check (logic demonstrated)

---

## ▶️ How to Run Locally

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt

---

## ⚙️ Tech Stack

- **Python**
- **Pandas / NumPy**
- **Scikit-learn**
- **LightGBM**
- **FastAPI**
- **Uvicorn**
- **Streamlit**
- **Matplotlib / Seaborn**
- **Git & GitHub**

---

## 🌐 Web Application Features

### 1️⃣ Applicant Risk Prediction
- Input applicant details
- Get:
  - Probability of default
  - Risk score
  - Risk band
  - Loan decision

### 2️⃣ Portfolio Risk Dashboard
- Histogram of predicted risk scores
- Model performance metrics (AUC & KS)
- Business insight charts
- Fairness check (logic demonstrated)

---

## ▶️ How to Run Locally

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
