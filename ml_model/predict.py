# ml_model/predict.py
import sys
import json
import joblib
import pandas as pd


model = joblib.load("diabetes_model.pkl")


data = json.loads(sys.stdin.read())


df = pd.DataFrame([data])



# Predict probability
proba = model.predict_proba(df)[0, 1]
prediction = int(proba >= 0.5)

# Output result as JSON
print(json.dumps({
    "prediction": prediction,
    "probability": float(proba)
}))
