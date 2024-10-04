# src/visualize.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def visualize_data(df, output_dir):
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    
    for col in categorical_columns:
        plt.figure(figsize=(10, 5))
        sns.countplot(x=col, data=df)
        plt.title(f'Distribution of {col}')
        plt.xticks(rotation=45)
        plt.savefig(f"{output_dir}/{col}_distribution.png")
        plt.close()

if __name__ == "__main__":
    df = pd.read_csv(r"../data/covid_toy.csv")
    visualize_data(df, output_dir="../visualizations")
