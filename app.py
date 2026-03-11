import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("models/breast_cancer_model.pkl", "rb"))

# Page configuration
st.set_page_config(page_title="Breast Cancer AI Detector", layout="wide")

# Custom CSS for background and font
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Background gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

/* Make text visible */
label, p, h1, h2, h3, h4, h5, h6, span {
    color: white !important;
}

/* Slider label */
.stSlider label {
    color: white !important;
    font-weight: 500;
}

/* Button styling */
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    font-size: 18px;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🧬 AI Breast Cancer Detection System")

st.write("Adjust the tumor characteristics below to predict whether the tumor is **Benign or Malignant**.")

# Feature names
feature_names = [
    "mean radius","mean texture","mean perimeter","mean area","mean smoothness",
    "mean compactness","mean concavity","mean concave points","mean symmetry","mean fractal dimension",
    "radius error","texture error","perimeter error","area error","smoothness error",
    "compactness error","concavity error","concave points error","symmetry error","fractal dimension error",
    "worst radius","worst texture","worst perimeter","worst area","worst smoothness",
    "worst compactness","worst concavity","worst concave points","worst symmetry","worst fractal dimension"
]

features = []

# Sliders remain unchanged
for feature in feature_names:
    value = st.slider(feature, 0.0, 1000.0, 0.0)
    features.append(value)

st.divider()

# Prediction
if st.button("🔍 Predict Tumor Type"):

    prediction = model.predict([features])
    probability = model.predict_proba([features])

    if prediction[0] == 1:
        st.error(f"⚠️ Malignant Tumor Detected\n\nConfidence: {probability[0][1]*100:.2f}%")
    else:
        st.success(f"✅ Benign Tumor Detected\n\nConfidence: {probability[0][0]*100:.2f}%")

    st.progress(int(max(probability[0])*100))