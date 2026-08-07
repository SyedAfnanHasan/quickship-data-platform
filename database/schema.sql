CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    product VARCHAR(100),
    amount DECIMAL(10,2),

    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);

CREATE TABLE IF NOT EXISTS deliveries (
    delivery_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    driver_id INTEGER,
    delivery_date DATE,
    delivery_time_minutes INTEGER,

    FOREIGN KEY (order_id)
    REFERENCES orders(order_id)
);