from cv2 import dnn_DetectionModel
import pandas as pd
import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=newuser password=password")

cur = conn.cursor()

df = pd.read_csv('NewDatasets/treats.csv', header=None)
cur.execute("CREATE TABLE Treats (drugId text, indicationId text, PRIMARY KEY (drugId, indicationId), FOREIGN KEY (drugId) REFERENCES Drugs, FOREIGN KEY (indicationId) REFERENCES Indications);")
for i in range(0, len(df)):
    drugId = df.iloc[i,0]
    indicationId = df.iloc[i,1]
    print("{0} : {1}".format(drugId, indicationId))
    cur.execute("INSERT INTO Treats (drugId, indicationId) VALUES ('{0}', '{1}');".format(drugId, indicationId))

conn.commit()

# Close communication with the database
cur.close()
conn.close()