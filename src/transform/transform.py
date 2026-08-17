import pandas as pd

from src.utils.logger import get_logger


logger = get_logger(__name__)


def transform_customers(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Transform customer data.
    """
    logger.info("Starting customer transformation")

    customers = customers.copy()

    customers["name"] = customers["name"].str.strip()

    customers["signup_date"] = pd.to_datetime(
        customers["signup_date"],
        errors="raise"
    )

    logger.info("Customer transformation completed")

    return customers

def transform_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Transform order data.
    """
    logger.info("Starting order transformation")

    orders = orders.copy()

    orders["amount"] = pd.to_numeric(
        orders["amount"],
        errors="raise"
    )

    orders["order_date"] = pd.to_datetime(
        orders["order_date"],
        errors="raise"
    )

    logger.info("Order transformation completed")

    return orders

def transform_deliveries(
    deliveries: pd.DataFrame
) -> pd.DataFrame:
    """
    Transform delivery data.
    """
    logger.info("Starting delivery transformation")

    deliveries = deliveries.copy()

    deliveries["delivery_time_minutes"] = pd.to_numeric(
        deliveries["delivery_time_minutes"],
        errors="raise"
    )

    deliveries["delivery_date"] = pd.to_datetime(
        deliveries["delivery_date"],
        errors="raise"
    )

    logger.info("Delivery transformation completed")

    return deliveries

def transform_drivers(drivers: pd.DataFrame) -> pd.DataFrame:
    """
    Transform driver data.
    """
    drivers = drivers.copy()

    drivers["driver_id"] = drivers["driver_id"].astype(int)
    drivers["name"] = drivers["name"].astype(str)
    drivers["city"] = drivers["city"].astype(str)
    drivers["hire_date"] = pd.to_datetime(drivers["hire_date"])

    return drivers