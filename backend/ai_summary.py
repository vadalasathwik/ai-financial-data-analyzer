import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="trading_db",
    user="postgres",
    password="sathwik@2025"
)

cursor = conn.cursor()

query = """
SELECT stock, SUM(volume) AS total_volume
FROM trades
GROUP BY stock
ORDER BY total_volume DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nAI Trading Insights\n")

top_stock = results[0]

print(f"Top traded stock: {top_stock[0]} with {top_stock[1]} shares.\n")

print("Trading Volume Breakdown:")

for row in results:
    print(f"{row[0]} traded {row[1]} shares")

print("\nInsight:")
print(f"{top_stock[0]} shows the highest trading activity, indicating stronger market interest compared to other stocks.")

cursor.close()
conn.close()