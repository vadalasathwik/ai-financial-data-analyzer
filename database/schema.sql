CREATE TABLE trades (
    trade_id INT PRIMARY KEY,
    stock VARCHAR(10),
    price FLOAT,
    volume INT,
    date DATE
);