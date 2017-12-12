import psycopg2
#Connect to an existing database
conn = psycopg2.connect("host=10.10.100.241 dbname= billing user=reader password = superpuper")
# Open a cursor to perform database operations
cur = conn.cursor()
# Query the database and obtain data as Python objects
cur.execute("select * from tarif_plans;")
results2 = cur.fetchall()

for record in results2:
    print(record)

# Close communication with the database
cur.close()
conn.close()