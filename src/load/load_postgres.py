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
    Incrementally load customer data into the customers table.
    """
    existing_ids = get_existing_ids(
        "customers",
        "customer_id"
    )

    new_customers = customers[
        ~customers["customer_id"].isin(existing_ids)
    ]

    if new_customers.empty:
        print("No new customers to load.")
        return

    load_dataframe(new_customers, "customers")

    print(f"Loaded {len(new_customers)} new customers.")

def load_orders(orders: pd.DataFrame) -> None:
    """
    Incrementally load order data into the orders table.
    """
    existing_ids = get_existing_ids(
        "orders",
        "order_id"
    )

    new_orders = orders[
        ~orders["order_id"].isin(existing_ids)
    ]

    if new_orders.empty:
        print("No new orders to load.")
        return

    load_dataframe(new_orders, "orders")

    print(f"Loaded {len(new_orders)} new orders.")

def load_deliveries(deliveries: pd.DataFrame) -> None:
    """
    Incrementally load delivery data into the deliveries table.
    """
    existing_ids = get_existing_ids(
        "deliveries",
        "delivery_id"
    )

    new_deliveries = deliveries[
        ~deliveries["delivery_id"].isin(existing_ids)
    ]

    if new_deliveries.empty:
        print("No new deliveries to load.")
        return

    load_dataframe(new_deliveries, "deliveries")

    print(f"Loaded {len(new_deliveries)} new deliveries.")

def is_table_empty(table_name: str) -> bool:
    query = f"SELECT EXISTS (SELECT 1 FROM {table_name})"

    with engine.connect() as connection:
        result = connection.exec_driver_sql(query)

    return not result.scalar()

def get_existing_ids(
    table_name: str,
    id_column: str
) -> set:
    """
    Get existing primary key values from a PostgreSQL table.
    """
    query = f"SELECT {id_column} FROM {table_name}"

    with engine.connect() as connection:
        result = connection.exec_driver_sql(query)

    return {row[0] for row in result}

def load_drivers(drivers: pd.DataFrame) -> None:
    """
    Incrementally load driver data into the drivers table.
    """
    existing_ids = get_existing_ids(
        "drivers",
        "driver_id"
    )

    new_drivers = drivers[
        ~drivers["driver_id"].isin(existing_ids)
    ]

    if new_drivers.empty:
        print("No new drivers to load.")
        return

    load_dataframe(new_drivers, "drivers")

    print(f"Loaded {len(new_drivers)} new drivers.")

if __name__ == "__main__":
    with engine.connect() as connection:
        print("PostgreSQL connection successful!")