import pandas as pd


def validate_unique_customer_ids(customers: pd.DataFrame) -> None:
    """
    Validate that customer IDs are unique.
    """
    if customers["customer_id"].duplicated().any():
        raise ValueError("Duplicate customer IDs found")

def validate_customer_ids_not_null(customers: pd.DataFrame) -> None:
    """
    Validate that customer IDs are not missing.
    """
    if customers["customer_id"].isna().any():
        raise ValueError("Missing customer IDs found")

def validate_unique_order_ids(orders: pd.DataFrame) -> None:
    """
    Validate that order IDs are unique.
    """
    if orders["order_id"].duplicated().any():
        raise ValueError("Duplicate order IDs found")

def validate_order_customer_ids(
    orders: pd.DataFrame,
    customers: pd.DataFrame
) -> None:
    """
    Validate that every customer ID in orders
    exists in the customers dataset.
    """
    invalid_customer_ids = set(orders["customer_id"]) - set(
        customers["customer_id"]
    )

    if invalid_customer_ids:
        raise ValueError(
            f"Orders contain unknown customer IDs: {invalid_customer_ids}"
        )

def validate_order_amounts(orders: pd.DataFrame) -> None:
    """
    Validate that order amounts are not negative.
    """
    if (orders["amount"] < 0).any():
        raise ValueError("Negative order amounts found")

def validate_order_ids_not_null(orders: pd.DataFrame) -> None:
    """
    Validate that order IDs and customer IDs are not missing.
    """
    required_columns = ["order_id", "customer_id"]

    if orders[required_columns].isna().any().any():
        raise ValueError(
            "Missing order_id or customer_id values found"
        )

def validate_unique_delivery_ids(
    deliveries: pd.DataFrame
) -> None:
    """
    Validate that delivery IDs are unique.
    """
    if deliveries["delivery_id"].duplicated().any():
        raise ValueError("Duplicate delivery IDs found")

def validate_delivery_order_ids(
    deliveries: pd.DataFrame,
    orders: pd.DataFrame
) -> None:
    """
    Validate that every order ID in deliveries
    exists in the orders dataset.
    """
    invalid_order_ids = set(deliveries["order_id"]) - set(
        orders["order_id"]
    )

    if invalid_order_ids:
        raise ValueError(
            f"Deliveries contain unknown order IDs: {invalid_order_ids}"
        )

def validate_delivery_times(
    deliveries: pd.DataFrame
) -> None:
    """
    Validate that delivery times are not negative.
    """
    if (deliveries["delivery_time_minutes"] < 0).any():
        raise ValueError("Negative delivery times found")

def validate_delivery_ids_not_null(
    deliveries: pd.DataFrame
) -> None:
    """
    Validate that delivery IDs and order IDs are not missing.
    """
    required_columns = ["delivery_id", "order_id"]

    if deliveries[required_columns].isna().any().any():
        raise ValueError(
            "Missing delivery_id or order_id values found"
        )

def validate_customers(customers: pd.DataFrame) -> None:
    """
    Run all customer validation rules.
    """
    validate_unique_customer_ids(customers)
    validate_customer_ids_not_null(customers)

def validate_orders(
    orders: pd.DataFrame,
    customers: pd.DataFrame
) -> None:
    """
    Run all order validation rules.
    """
    validate_unique_order_ids(orders)
    validate_order_ids_not_null(orders)
    validate_order_customer_ids(orders, customers)
    validate_order_amounts(orders)

def validate_deliveries(
    deliveries: pd.DataFrame,
    orders: pd.DataFrame
) -> None:
    """
    Run all delivery validation rules.
    """
    validate_unique_delivery_ids(deliveries)
    validate_delivery_ids_not_null(deliveries)
    validate_delivery_order_ids(deliveries, orders)
    validate_delivery_times(deliveries)