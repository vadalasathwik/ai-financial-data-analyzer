import pandas as pd
import psycopg2

# Load CSV dataset
df = pd.read_csv("../data/sample_trading_data.csv")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="trading_db",
    user="postgres",
    password="sathwik@2025"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO trades (trade_id, stock, price, volume, date)
        VALUES (%s,%s,%s,%s,%s)
        """,
        (row.trade_id, row.stock, row.price, row.volume, row.date)
    )

conn.commit()

cursor.close()
conn.close()

print("Data loaded successfully!")