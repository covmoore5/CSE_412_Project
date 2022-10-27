from cv2 import dnn_DetectionModel
import pandas as pd
import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=newuser password=password")

cur = conn.cursor()

df = pd.read_csv('NewDatasets/drug_se.csv', header=None)
cur.execute("CREATE TABLE DrugSe (drugId text, seId text, PRIMARY KEY (drugId, seId), FOREIGN KEY (drugId) REFERENCES Drugs, FOREIGN KEY (seId) REFERENCES SideEffects);")
for i in range(0, len(df)):
    drugId = df.iloc[i,0]
    seId = df.iloc[i,1]
    print("{0} : {1}".format(drugId, seId))
    cur.execute("INSERT INTO DrugSe (drugId, seId) VALUES ('{0}', '{1}');".format(drugId, seId))

conn.commit()

# Close communication with the database
cur.close()
conn.close()