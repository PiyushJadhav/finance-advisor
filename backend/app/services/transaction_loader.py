import pandas as pd

def load_transactions(file) -> pd.DataFrame:
    df = pd.read_csv(file, parse_dates=['date'])
    required = {'date','amount','category','merchant','type'}
    if not required.issubset(df.columns):
        raise ValueError("Invalid CSV format")
    return df
