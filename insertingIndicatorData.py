from cv2 import dnn_DetectionModel
import pandas as pd
import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=newuser password=password")

cur = conn.cursor()

df = pd.read_csv('NewDatasets/indications.csv', header=None)
cur.execute("CREATE TABLE Indications (indicationId text PRIMARY KEY, indicationName text);")
for i in range(0, len(df)):
    indicationId = df.iloc[i,0]
    indicationName = df.iloc[i,1]
    print("{0} : {1}".format(indicationId, indicationName))
    cur.execute("INSERT INTO Indications (indicationId, indicationName) VALUES ('{0}', '{1}');".format(indicationId, indicationName))

conn.commit()

# Close communication with the database
cur.close()
conn.close()