import psycopg2

# Параметры подключения к базе данных PostgreSQL
conn = psycopg2.connect(
    dbname="testdb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT version();")
print("Версия PostgreSQL:", cur.fetchone())

cur.close()
conn.close()
