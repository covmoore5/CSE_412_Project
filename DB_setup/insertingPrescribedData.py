from cv2 import dnn_DetectionModel
import pandas as pd
import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=password")

cur = conn.cursor()

df = pd.read_csv('NewDatasets/prescribed.csv')

cur.execute("CREATE TABLE Prescribed (pId text, drugId text, PRIMARY KEY (pId, drugId), FOREIGN KEY (pId) REFERENCES Patients, FOREIGN KEY (drugID) REFERENCES Drugs );")
for i in range(0, len(df)):
    pId = df.iloc[i,0]
    drugId = df.iloc[i,1]
    print("{0} : {1}".format(pId, drugId))
    cur.execute("INSERT INTO Prescribed (pId, drugId) VALUES ('{0}', '{1}');".format(pId, drugId))

conn.commit()

# Close communication with the database
cur.close()
conn.close()
