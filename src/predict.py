import os
import pickle
import numpy as np

base_dir = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(base_dir, "models", "breast_cancer_model.pkl")

model = pickle.load(open(model_path, "rb"))

def predict_cancer(features):

    prediction = model.predict([features])

    if prediction[0] == 1:
        return "Malignant"
    else:
        return "Benign"


if __name__ == "__main__":

    sample = [0.1] * 30

    result = predict_cancer(sample)

    print("Prediction:", result)