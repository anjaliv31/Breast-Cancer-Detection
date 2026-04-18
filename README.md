# 🧬 AI Breast Cancer Detection System

## 🚀 Overview
This project is an end-to-end Machine Learning system designed to classify tumors as **benign or malignant** using medical diagnostic data.

The system focuses on **model comparison, performance evaluation, and real-time deployment** through an interactive web application built with Streamlit.

---

## 📊 Dataset
The model is trained on the **Breast Cancer Wisconsin Dataset**, which contains features computed from digitized images of fine needle aspirates of breast masses.

### Features include:
- Mean radius  
- Mean texture  
- Mean perimeter  
- Mean area  
- Smoothness  
- Compactness  
- Concavity  
- Symmetry  
- Fractal dimension  

**Total features:** 30  

### Target Classes:
- **Benign (Non-Cancerous)**  
- **Malignant (Cancerous)**  

---

## 🤖 Models Implemented & Results

The following machine learning models were trained and evaluated:

- Logistic Regression — **97.37%**
- K-Nearest Neighbors (KNN) — **94.73%**
- Decision Tree — **92.10%**
- Random Forest — **96.49%**
- Support Vector Machine (SVM) — **98.25%** ⭐

👉 **SVM achieved the highest accuracy and was selected as the final model.**

---

## 📈 Model Performance

- **Best Model:** Support Vector Machine (SVM)  
- **Accuracy:** **98.25%**

The model was evaluated on unseen test data to ensure strong generalization and reliability.

---

## 🖥️ Web Application

The trained model is deployed as an interactive dashboard using **Streamlit**.

### Features:
- Adjustable tumor characteristics using sliders  
- Real-time prediction (Benign / Malignant)  
- Confidence score display  
- Fast and user-friendly interface  

---

## 🏗️ System Design

- Data preprocessing and feature scaling  
- Model training and evaluation pipeline  
- Model serialization using `.pkl`  
- Prediction logic implemented in `predict.py`  
- Interactive frontend using Streamlit  

---

## 📁 Project Structure

Breast-Cancer-Detection
│
├── app.py
├── requirements.txt
├── README.md
│
├── models
│   └── breast_cancer_model.pkl
│
├── notebooks
│   └── model_training.ipynb
│
├── src
│   └── predict.py
│
└── results
    └── app_screenshot.png

---

## ⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/breast-cancer-detection.git  
cd breast-cancer-detection  

Install dependencies:

pip install -r requirements.txt  

---

## ▶️ Run the Application

streamlit run app.py  

Open in browser:  
http://localhost:8501  

---

## 📸 Application Preview

- Interactive dashboard for tumor input  
- Real-time prediction with confidence score  

---

## 🛠️ Tech Stack

- Python  
- Scikit-learn  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Streamlit  

---

## 🎯 Key Highlights

- End-to-end ML pipeline with deployment  
- Comparison of multiple ML algorithms  
- High accuracy classification model (**98.25%**)  
- Real-time prediction system  

---

## 🚀 Future Improvements

- Add model explainability (SHAP / feature importance)  
- Deploy application online (Streamlit Cloud / AWS)  
- Integrate larger real-world medical datasets  
- Convert into REST API using FastAPI  

---

## 💡 Conclusion

This project demonstrates the ability to:
- Build and evaluate machine learning models  
- Select optimal models based on performance  
- Deploy ML solutions into interactive applications  
- Translate data science concepts into practical systems  
