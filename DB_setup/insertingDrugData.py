import pandas as pd
import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=newuser password=password")

cur = conn.cursor()

df = pd.read_csv('Datasets/drug_names.tsv', sep='\t', header=None)

cur.execute("CREATE TABLE Drugs (drugId text PRIMARY KEY, drugName text);")
for i in range(0, len(df)):
    drugId = df.iloc[i,0]
    drugName = df.iloc[i,1]
    print("{0} : {1}".format(drugId, drugName))
    cur.execute("INSERT INTO Drugs (drugId, drugName) VALUES ('{0}', '{1}');".format(drugId, drugName))

conn.commit()

# Close communication with the database
cur.close()
conn.close()