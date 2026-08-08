# 🔧 AI-Based Predictive Maintenance System

## 📌 Project Overview

The AI-Based Predictive Maintenance System is a machine learning-powered web application developed using Streamlit. The system helps industries predict equipment failures before they occur by analyzing machine operating parameters and historical maintenance data.

This project was developed as part of Vocational Training at NTPC Farakka under the Information Technology Department.

---

## 🎯 Objectives

- Predict machine failures before breakdowns occur.
- Reduce maintenance costs and downtime.
- Improve equipment reliability and availability.
- Provide an interactive dashboard for data analysis.
- Enable maintenance engineers to make data-driven decisions.

---

## 🚀 Features

### 📂 Dataset Upload
- Upload predictive maintenance datasets in CSV format.
- View dataset preview.
- Validate uploaded data.

### 📊 Data Analysis Dashboard
- Dataset summary statistics.
- Missing value analysis.
- Failure distribution visualization.
- Correlation heatmap.
- Feature statistics.

### 🤖 Model Training
- Random Forest Classifier.
- Train/Test split.
- Performance evaluation using:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
- Confusion Matrix.

### 🔍 Prediction Module
- Enter machine parameters manually.
- Predict equipment condition.
- Display maintenance recommendations.

Prediction Categories:

| Status | Description |
|----------|------------|
| 🟢 Healthy | Low failure probability |
| 🟡 Warning | Medium failure probability |
| 🔴 Maintenance Required | High failure probability |

---

## 🏗️ Project Architecture

```text
Dataset Upload
       ↓
Data Analysis
       ↓
Model Training
       ↓
Model Saving
       ↓
Prediction Dashboard
```

---

## 🛠️ Technology Stack

### Frontend
- Streamlit

### Backend
- Python

### Libraries
- Pandas
- NumPy
- Scikit-Learn
- Plotly
- Joblib

---

## 📁 Project Structure

```text
Predictive_Maintenance_System/

│
├── app.py
│
├── pages/
│   ├── 1_Upload_dataset.py
│   ├── 2_Data_Analysis.py
│   ├── 3_Model_Training.py
│   └── 4_Prediction.py
│
├── models/
│
├── dataset/
│
├── reports/
│
├── requirements.txt
│
└── README.md
```

---

## 📊 Dataset

The project is demonstrated using the AI4I 2020 Predictive Maintenance Dataset.

Main Features:

- Air Temperature [K]
- Process Temperature [K]
- Rotational Speed [rpm]
- Torque [Nm]
- Tool Wear [min]

Target Variable:

- Machine Failure

The system can be extended to support other predictive maintenance datasets.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd Predictive_Maintenance_System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📈 Workflow

1. Upload Dataset
2. Analyze Dataset
3. Train Machine Learning Model
4. Evaluate Performance
5. Predict Equipment Health Status

---

- Dataset Upload Page
- Data Analysis Dashboard
- Correlation Heatmap
- Model Training Results
- Prediction Dashboard

---

## 🔮 Future Scope

- IoT Sensor Integration
- Real-Time Data Monitoring
- Cloud Deployment
- Deep Learning Models
- Mobile Application
- Automated Maintenance Scheduling

---

## 🎓 Academic Information

**Project Title:** AI-Based Predictive Maintenance System

**Student:** Tapaswini Shaw

**UEN:** RTU24101CS024

**Branch:** B.Tech CSE AIML

**College:** Rai Technology University

**Organization:** NTPC Farakka

**Training Duration:** 22 July 2026 – 11 August 2026

---

## 📚 References

1. AI4I 2020 Predictive Maintenance Dataset
2. Python Documentation
3. Streamlit Documentation
4. Scikit-Learn Documentation
5. Pandas Documentation

---