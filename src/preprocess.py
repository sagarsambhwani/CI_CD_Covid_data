# src/preprocess.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    
    # Handle missing values (if any)
    df = df.dropna()
    
    # Label encoding of categorical columns
    le = LabelEncoder()
    categorical_columns = df.select_dtypes(include=['object']).columns
    
    for col in categorical_columns:
        df[col] = le.fit_transform(df[col])
    
    return df

if __name__ == "__main__":
    filepath = r"../data/covid_toy.csv"
    df = load_and_preprocess_data(filepath)
    print(df.head())
