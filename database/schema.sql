CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(150),
    city VARCHAR(50),
    signup_date DATE
);

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

    FOREIGN KEY (driver_id)
    REFERENCES drivers(driver_id)
);

CREATE TABLE IF NOT EXISTS drivers (
    driver_id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50),
    hire_date DATE
);