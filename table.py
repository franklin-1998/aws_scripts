import psycopg2
# connecting flask


#initializing postgresql database
conn = psycopg2.connect(database="remote_efficiency_db", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5433")
cur = conn.cursor()
cur.execute('''CREATE TABLE user_credentials
      (user_id SERIAL primary key NOT NULL,
      username varchar(100),
      companyname varchar(100) NOT NULL,
      mailid varchar(50) NOT NULL UNIQUE,
      password varchar(50),
      timestamp text);''')
conn.commit()
print("\n\nUserDetails Table created successfully\n\n")