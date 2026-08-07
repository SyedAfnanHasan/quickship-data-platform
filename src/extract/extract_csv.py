import pandas as pd
from pathlib import Path

# Path to the raw data folder
RAW_DATA_PATH = Path("data/raw")


def extract_customers():
    return pd.read_csv(RAW_DATA_PATH / "customers.csv")


def extract_orders():
    return pd.read_csv(RAW_DATA_PATH / "orders.csv")


def extract_deliveries():
    return pd.read_csv(RAW_DATA_PATH / "deliveries.csv")