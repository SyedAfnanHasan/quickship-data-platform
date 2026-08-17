import pandas as pd

from src.config.config import RAW_DATA_PATH
from src.utils.logger import get_logger

logger = get_logger(__name__)

def extract_customers() -> pd.DataFrame:
    """
    Extract customer data from CSV file.
    """
    file_path = RAW_DATA_PATH / "customers.csv"

    logger.info("Starting customer extraction")

    try:
        customers = pd.read_csv(file_path)

    except FileNotFoundError:
        logger.error("Customer file not found: %s", file_path)
        raise

    logger.info("Customers extracted: %d rows", len(customers))

    return customers

def extract_orders() -> pd.DataFrame:
    """
    Extract order data from CSV file.
    """
    file_path = RAW_DATA_PATH / "orders.csv"

    logger.info("Starting order extraction")

    try:
        orders = pd.read_csv(file_path)

    except FileNotFoundError:
        logger.error("Orders file not found: %s", file_path)
        raise

    logger.info("Orders extracted: %d rows", len(orders))

    return orders


def extract_deliveries() -> pd.DataFrame:
    """
    Extract delivery data from CSV file.
    """
    file_path = RAW_DATA_PATH / "deliveries.csv"

    logger.info("Starting delivery extraction")

    try:
        deliveries = pd.read_csv(file_path)

    except FileNotFoundError:
        logger.error("Delivery file not found: %s", file_path)
        raise

    logger.info("Deliveries extracted: %d rows", len(deliveries))

    return deliveries

def extract_drivers() -> pd.DataFrame:
    """
    Extract driver data from CSV file.
    """
    file_path = RAW_DATA_PATH / "drivers.csv"

    logger.info("Starting driver extraction")

    try:
        drivers = pd.read_csv(file_path)

    except FileNotFoundError:
        logger.error("Driver file not found: %s", file_path)
        raise

    logger.info("Drivers extracted: %d rows", len(drivers))

    return drivers