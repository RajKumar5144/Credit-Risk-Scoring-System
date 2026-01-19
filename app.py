from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load model & columns
model = joblib.load("lgb_model.pkl")
columns = joblib.load("columns.pkl")


def risk_band(score):
    if score <= 300:
        return "Low Risk"
    elif score <= 600:
        return "Medium Risk"
    else:
        return "High Risk"

def loan_decision(score):
    if score <= 500:
        return "Approve"
    elif score <= 650:
        return "Manual Review"
    else:
        return "Reject"

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])

    # One-hot encode
    df = pd.get_dummies(df)

    # Align columns
    df = df.reindex(columns=columns, fill_value=0)

    # Predict probability
    pd_default = model.predict_proba(df)[:, 1][0]
    risk_score = int(pd_default * 1000)

    return {
        "probability_of_default": round(pd_default, 3),
        "risk_score": risk_score,
        "risk_band": risk_band(risk_score),
        "loan_decision": loan_decision(risk_score)
    }
