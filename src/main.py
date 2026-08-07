from extract.extract_csv import (
    extract_customers,
    extract_orders,
    extract_deliveries,
)


def main():
    customers = extract_customers()
    orders = extract_orders()
    deliveries = extract_deliveries()

    print("Customers")
    print(customers.head())

    print("\nOrders")
    print(orders.head())

    print("\nDeliveries")
    print(deliveries.head())


if __name__ == "__main__":
    main()