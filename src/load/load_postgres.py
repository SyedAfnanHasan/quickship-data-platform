from sqlalchemy import create_engine
import pandas as pd

from src.config.config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

def load_dataframe(
    df: pd.DataFrame,
    table_name: str
) -> None:
    """
    Load a DataFrame into a PostgreSQL table.
    """
    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )

def load_customers(customers: pd.DataFrame) -> None:
    """
    Load customer data into the customers table.
    """
    load_dataframe(customers, "customers")

def load_orders(orders: pd.DataFrame) -> None:
    """
    Load order data into the orders table.
    """
    load_dataframe(orders, "orders")

def load_deliveries(deliveries: pd.DataFrame) -> None:
    """
    Load delivery data into the deliveries table.
    """
    load_dataframe(deliveries, "deliveries")

def is_table_empty(table_name: str) -> bool:
    query = f"SELECT EXISTS (SELECT 1 FROM {table_name})"

    with engine.connect() as connection:
        result = connection.exec_driver_sql(query)

    return not result.scalar()

if __name__ == "__main__":
    with engine.connect() as connection:
        print("PostgreSQL connection successful!")