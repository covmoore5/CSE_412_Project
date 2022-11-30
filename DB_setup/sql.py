import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=newuser password=password")

cur = conn.cursor()
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

conn.commit()

# Close communication with the database
cur.close()
conn.close()