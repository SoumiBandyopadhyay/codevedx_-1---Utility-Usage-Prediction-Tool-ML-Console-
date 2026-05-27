import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

FILE_PATH = "../data/usage_data.csv"

def train_model():
    df = pd.read_csv(FILE_PATH)

    X = df[["month"]]
    y = df["units_used"]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, "../models/model.pkl")

    print("Model trained successfully!")

def predict_usage():
    model = joblib.load("../models/model.pkl")

    future_month = int(input("Enter future month: "))

    prediction = model.predict([[future_month]])

    print(f"Predicted Usage: {prediction[0]:.2f} units")
