# 🧬 AI Breast Cancer Detection System

## 📌 Overview

This project is a **Machine Learning-based Breast Cancer Detection System** that predicts whether a tumor is **benign or malignant** based on tumor characteristics.

The model is trained using the **Breast Cancer Wisconsin Dataset** and deployed as an interactive web application using Streamlit. Users can adjust tumor features through sliders and receive a **real-time prediction** along with confidence scores.

---

## 📊 Dataset

This project uses the **Breast Cancer Wisconsin Dataset**, which contains medical measurements of tumor cell nuclei.

Features include:

* Mean radius
* Mean texture
* Mean perimeter
* Mean area
* Smoothness
* Compactness
* Concavity
* Symmetry
* Fractal dimension

Total features used: **30**

Target classes:

* **Benign (Non-Cancerous)**
* **Malignant (Cancerous)**

---

## 🤖 Machine Learning Models Used

The following machine learning models were implemented and compared:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)

After evaluation, **Random Forest** provided the best performance and was selected as the final model.

---

## 🖥️ Web Application

The trained model is deployed as an interactive dashboard using Streamlit where users can:

* Adjust tumor characteristics using sliders
* Run predictions instantly
* View prediction confidence

---

## 📁 Project Structure

```
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
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/breast-cancer-detection.git
cd breast-cancer-detection
```

Install required libraries:

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```
streamlit run app.py
```

Then open in your browser:

```
http://localhost:8501
```

---

## 📸 Application Screenshot

### Dashboard
![Dashboard](results/dashboard.png)

### Prediction Result
![Prediction Result](results/result.png)

---

## 🚀 Features

* End-to-end machine learning pipeline
* Multiple model comparison
* Random Forest model deployment
* Interactive AI dashboard
* Real-time tumor classification

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit

---

## 🎯 Future Improvements

* Add model explainability (SHAP / feature importance visualization)
* Improve UI with advanced dashboards
* Deploy application publicly for live access
* Integrate larger medical datasets

---


