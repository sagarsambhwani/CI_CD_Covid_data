# src/main.py

from preprocess import load_and_preprocess_data
from visualize import visualize_data
from train_model import train_model
import os

if __name__ == "__main__":
    # File paths
    data_file = "../data/covid_toy.csv"
    visualization_dir = "../visualizations"
    model_dir = "../models"
    
    # Ensure directories exist
    os.makedirs(visualization_dir, exist_ok=True)
    os.makedirs(model_dir, exist_ok=True)
    
    # Step 1: Preprocess the data
    df = load_and_preprocess_data(data_file)
    
    # Step 2: Visualize the data
    visualize_data(df, visualization_dir)
    
    # Step 3: Train the model
    model = train_model(df)
