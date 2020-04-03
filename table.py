import psycopg2
# connecting flask


#initializing postgresql database
conn = psycopg2.connect(database="remote_efficiency_db", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5433")
cur = conn.cursor()