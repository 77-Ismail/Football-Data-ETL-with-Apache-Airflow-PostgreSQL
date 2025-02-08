import pandas as pd

def extract():
    file_path = "raw_data/football_results.csv"
    df = pd.read_csv(file_path)
    print("✅ Data extracted successfully!")
    return df

