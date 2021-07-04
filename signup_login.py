import sqlite3
import tkinter as tk
from tkinter.constants import N
import bcrypt

#creating signup function for new users.
def signup():
    #connecting tothe database
    conn = sqlite3.connect('userdata.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS userdata(username VARCHAR PRIMARY KEY, password VARCHAR NOT NULL, email_address VARCHAR NOT NULL, contact_no VARCHAR NOT NULL)""")
    
    # taking inputs from the user
    un = input('Enter username:' )
    pa = input('Enter password:' )
    ea = input('Enter email address:' )
    cn = input('Enter contact no:' )
    
    #encrypting password
    pa = pa.encode()      
    salt = bcrypt.gensalt(14)               
    password_hash_bytes = bcrypt.hashpw(pa, salt)   
    pa = password_hash_bytes.decode()   
    
    #checking if contact number is valid
    firstdigit = int(cn[0])
    while len(cn) != 10:
        print('Phone number should be 10 characters long, Please try again.')
        cn = input('Enter contact no:' )
        
      
    while firstdigit < 6:
        print('Phone number should not start with', firstdigit, 'Please try again.')
        cn = input('Enter contact no:' )
        firstdigit = int(cn[0])
         
    
    #checking if username entered already exists and it it does taking another input
    c.execute("SELECT 1 FROM userdata WHERE username=?", (un,))
    while len(c.fetchall()) > 0:
        print('Username already exists, please try again')
        un = input('Enter username:' )
        pa = input('Enter password:' )
        c.execute("SELECT 1 FROM userdata WHERE username=?", (un,))
    c.execute("""INSERT INTO userdata(username,password,email_address,contact_no) VALUES (?,?,?,?)""", (un, pa, ea, cn))    
    print('registration sucessfull') 
    conn.commit()
    conn.close()


#creating login function
def login():
    conn = sqlite3.connect('userdata.db')
    c = conn.cursor()
    
    #taking username password input from user
    un = input('Enter username:' )
    pa = input('Enter password:' )   
    c.execute("SELECT 1 FROM userdata WHERE username=? AND password=?", (un, pa)) 
    
    #if username or password is wrong
    while len(c.fetchall()) == 0:
        print('Incorrect username or password, please try again')
        un = input('Enter username:' )
        pa = input('Enter password:' )
        c.execute("SELECT 1 FROM userdata WHERE username=? AND password=?", (un, pa))

    #if username and password is correct
    print('welcome',un)


    conn.commit()
    conn.close()
    
print('Are you new user or existing user')
a = int(input('1 for new user \n 2 for existing user \n give input '))
if a == 1:
    signup()
else:
    login()    
         