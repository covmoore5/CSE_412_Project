import psycopg2

def find_ind_for_med(medicine_name):
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=password")
    cur = conn.cursor()
    cur.execute(" \
    SELECT Indications.indicationName \
    FROM Indications, Treats, Drugs \
    WHERE Indications.indicationId = Treats.indicationId \
    AND Treats.drugID = Drugs.drugId \
    AND Drugs.drugName = '{0}';".format(medicine_name))

    rows = cur.fetchall()


    # Close communication with the database
    cur.close()
    conn.close()

    return rows

def find_se_for_med(medicine_name):
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=password")
    cur = conn.cursor()
    cur.execute(" \
    SELECT SideEffects.seName \
    FROM SideEffects, DrugSe, Drugs \
    WHERE SideEffects.seId = DrugSe.seId \
    AND DrugSe.drugId = Drugs.drugId \
    AND Drugs.drugName = '{0}';".format(medicine_name))

    rows = cur.fetchall()


    # Close communication with the database
    cur.close()
    conn.close()

    return rows

def find_patient_presc(patient_name):
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=password")
    cur = conn.cursor()
    cur.execute(" \
    SELECT Drugs.drugName \
    FROM Drugs, Prescribed, Patients \
    WHERE Drugs.drugId = Prescribed.drugId \
    AND Prescribed.pId = Patients.pId \
    AND Patients.pName = '{0}';".format(patient_name))

    rows = cur.fetchall()


    # Close communication with the database
    cur.close()
    conn.close()

    return rows

def get_all_patients():
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=password")
    cur = conn.cursor()
    cur.execute(" \
    SELECT pName,pId \
    FROM Patients;")

    rows = cur.fetchall()


    # Close communication with the database
    cur.close()
    conn.close()

    return rows

def get_med_with_ind(indicationName):
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=password")
    cur = conn.cursor()
    cur.execute(" \
    SELECT Drugs.drugName \
    FROM Drugs, Treats, Indications \
    WHERE Drugs.drugId = Treats.drugId \
    AND Treats.indicationId = Indications.indicationId \
    AND Indications.indicationName = '{0}';".format(indicationName))

    rows = cur.fetchall()


    # Close communication with the database
    cur.close()
    conn.close()

    return rows
