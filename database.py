import sqlite3

conn = sqlite3.connect('userdata.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS userdata(username VARCHAR PRIMARY KEY, password VARCHAR NOT NULL, email_address VARCHAR NOT NULL, contact_no VARCHAR NOT NULL)""")
    
    
conn.commit()
conn.close()    
    