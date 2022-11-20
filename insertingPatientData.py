from cv2 import dnn_DetectionModel
import pandas as pd
import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=newuser password=password")

cur = conn.cursor()

df = pd.read_csv('NewDatasets/patients.csv')

cur.execute("CREATE TABLE Patients (pId text PRIMARY KEY, pName text NOT NULL, phoneNumber text NOT NULL);")
for i in range(0, len(df)):
    pName = df.iloc[i,1] + "," +  df.iloc[i,0]
    phoneNumber = df.iloc[i,2]
    pId = df.iloc[i,3]
    print("{0} : {1} : {2}".format(pName, phoneNumber, pId))
    cur.execute("INSERT INTO Patients (pId, pName, phoneNumber) VALUES ('{0}', '{1}', {2});".format(pId, pName, phoneNumber))

conn.commit()

# Close communication with the database
cur.close()
conn.close()
