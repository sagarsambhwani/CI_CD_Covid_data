# tests/test_preprocessing.py

from src.preprocess import load_and_preprocess_data

def test_load_and_preprocess_data():
    df = load_and_preprocess_data(r"../data/covid_toy.csv")
    assert not df.isnull().values.any(), "There should be no missing values!"
    assert df.select_dtypes(include=['object']).empty, "There should be no categorical data after preprocessing!"
