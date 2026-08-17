
from src.validation.validation import (
    validate_customers,
    validate_orders,
    validate_deliveries,
    validate_drivers,
)

from src.transform.transform import (
    transform_customers,
    transform_orders,
    transform_deliveries,
    transform_drivers,
)

from src.extract.extract_csv import (
    extract_customers,
    extract_orders,
    extract_deliveries,
    extract_drivers,
)

from src.load.load_postgres import (
    load_customers,
    load_orders,
    load_deliveries,
    load_drivers,
)

def main():
    customers = extract_customers()
    validate_customers(customers)
    customers = transform_customers(customers)

    load_customers(customers)

    orders = extract_orders()
    validate_orders(orders, customers)
    orders = transform_orders(orders)

    load_orders(orders)

    deliveries = extract_deliveries()
    validate_deliveries(deliveries, orders)
    deliveries = transform_deliveries(deliveries)

    load_deliveries(deliveries)


    drivers = extract_drivers()
    validate_drivers(drivers)
    drivers = transform_drivers(drivers)

    load_drivers(drivers)

if __name__ == "__main__":
    main()