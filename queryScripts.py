import psycopg2


conn = psycopg2.connect("host=localhost dbname=postgres user=newuser password=password")
cur = conn.cursor()

cur.execute(" \
SELECT Indications.indicationName \
FROM Indications, Treats, Drugs \
WHERE Indications.indicationId = Treats.indicationId \
AND Treats.drugID = Drugs.drugId \
AND Drugs.drugName = ‘penicillin’;")

rows = cur.fetchall()

print(rows)



# Close communication with the database
cur.close()
conn.close()