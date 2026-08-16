
from src.validation.validation import (
    validate_customers,
    validate_orders,
    validate_deliveries,
)

from src.transform.transform import (
    transform_customers,
    transform_orders,
    transform_deliveries,
)

from src.extract.extract_csv import (
    extract_customers,
    extract_orders,
    extract_deliveries,
)

from src.load.load_postgres import (
    load_customers,
    load_orders,
    is_table_empty,
    load_deliveries
)

def main():
    customers = extract_customers()
    validate_customers(customers)

    customers = transform_customers(customers)
    print("\nTransformed customers:")

    if is_table_empty("customers"):
        load_customers(customers)

    else:
        print("Customers table is not empty. Skipping customer load.")

    print(customers.dtypes)

    orders = extract_orders()
    validate_orders(orders, customers)

    orders = transform_orders(orders)
    print("\nTransformed orders:")

    if is_table_empty("orders"):
        load_orders(orders)
    else:
        print("Orders table is not empty. Skipping order load.")

    print(orders.dtypes)

    deliveries = extract_deliveries()
    validate_deliveries(deliveries, orders)

    deliveries = transform_deliveries(deliveries)
    print("\nTransformed deliveries:")

    if is_table_empty("deliveries"):
        load_deliveries(deliveries)
    else:
        print("Deliveries table is not empty. Skipping delivery load.")

    print(deliveries.dtypes)

    print("Customers")
    print(customers.head())

    print("\nOrders")
    print(orders.head())

    print("\nDeliveries")
    print(deliveries.head())


if __name__ == "__main__":
    main()