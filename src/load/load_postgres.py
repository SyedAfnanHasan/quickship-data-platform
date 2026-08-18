from sqlalchemy import create_engine, MetaData, Table, or_
from sqlalchemy.dialects.postgresql import insert
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

def upsert_dataframe(
    df: pd.DataFrame,
    table_name: str,
    primary_key: str
) -> None:
    """
    Insert new records or update existing records
    based on the primary key.
    """
    metadata = MetaData()

    table = Table(
        table_name,
        metadata,
        autoload_with=engine
    )

    records = df.to_dict(orient="records")

    if not records:
        return

    stmt = insert(table).values(records)

    update_columns = {
        column.name: stmt.excluded[column.name]
        for column in table.columns
        if column.name != primary_key
    }

    # stmt = stmt.on_conflict_do_update(
    #     index_elements=[primary_key],
    #     set_=update_columns
    # )

    changed_columns = [
        table.c[column.name].is_distinct_from(
            stmt.excluded[column.name]
        )
        for column in table.columns
        if column.name != primary_key
    ]

    stmt = stmt.on_conflict_do_update(
        index_elements=[primary_key],
        set_=update_columns,
        where=or_(*changed_columns)
    )

    with engine.begin() as connection:
        connection.execute(stmt)

def load_customers(customers: pd.DataFrame) -> None:
    """
    Upsert customer data into the customers table.
    """
    if customers.empty:
        print("No customers to load.")
        return

    upsert_dataframe(
        customers,
        "customers",
        "customer_id"
    )

    print(f"Upserted {len(customers)} customers.")

def load_orders(orders: pd.DataFrame) -> None:
    """
    Upsert order data into the orders table.
    """
    if orders.empty:
        print("No orders to load.")
        return

    upsert_dataframe(
        orders,
        "orders",
        "order_id"
    )

    print(f"Upserted {len(orders)} orders.")

def load_deliveries(deliveries: pd.DataFrame) -> None:
    """
    Upsert delivery data into the deliveries table.
    """
    if deliveries.empty:
        print("No deliveries to load.")
        return

    upsert_dataframe(
        deliveries,
        "deliveries",
        "delivery_id"
    )

    print(f"Upserted {len(deliveries)} deliveries.")

def load_drivers(drivers: pd.DataFrame) -> None:
    """
    Upsert driver data into the drivers table.
    """
    if drivers.empty:
        print("No drivers to load.")
        return

    upsert_dataframe(
        drivers,
        "drivers",
        "driver_id"
    )

    print(f"Upserted {len(drivers)} drivers.")

if __name__ == "__main__":
    with engine.connect() as connection:
        print("PostgreSQL connection successful!")