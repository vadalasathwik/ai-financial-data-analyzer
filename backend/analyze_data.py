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

for row in results:
    print(row)

cursor.close()
conn.close()