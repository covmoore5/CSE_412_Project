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


