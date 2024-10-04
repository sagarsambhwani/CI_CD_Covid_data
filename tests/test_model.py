# tests/test_model.py

from src.train_model import train_model
import pandas as pd

def test_train_model():
    df = pd.read_csv(r"../data/covid_toy.csv")
    model = train_model(df)
    assert model is not None, "Model should be trained and not None!"
