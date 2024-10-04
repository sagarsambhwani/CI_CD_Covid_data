# src/train_model.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd

def train_model(df):
    X = df.drop(columns='target')
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")
    
    # Save the model
    joblib.dump(model, "../models/rf_model.pkl")
    return model

if __name__ == "__main__":
    df = pd.read_csv(r"../data/covid_toy.csv")
    model = train_model(df)
