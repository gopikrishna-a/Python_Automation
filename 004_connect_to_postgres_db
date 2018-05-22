import psycopg2

myConnection = psycopg2.connect( host="127.0.0.1", user="postgres", password="postgres", dbname="contacts", sslmode="disable")
cur = myConnection.cursor()
cur.execute("SELECT version();")
cur.fetchall()
