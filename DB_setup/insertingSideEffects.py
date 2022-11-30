from cv2 import dnn_DetectionModel
import pandas as pd
import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=password")

cur = conn.cursor()

df = pd.read_csv('NewDatasets/sideEffects.csv', header=None)
cur.execute("CREATE TABLE SideEffects (seId text PRIMARY KEY, seName text);")
for i in range(0, len(df)):
    seId = df.iloc[i,0]
    seName = df.iloc[i,1]
    print("{0} : {1}".format(seId, seName))
    cur.execute("INSERT INTO SideEffects (seId, seName) VALUES ('{0}', '{1}');".format(seId, seName))

conn.commit()

# Close communication with the database
cur.close()
conn.close()