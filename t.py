from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import tkinter as tk
from tkinter.constants import N
import bcrypt



root=Tk()
root.title("LOGIN")


def submit():
    with sqlite3.connect("User_info.db") as db:
        cursor=db.cursor()

    cursor.execute("""INSERT INTO user_info VALUES(:username,:password,:email_address,:contact_no)""",
    {
        'user_name' :user_name.get(),
        'first_name' : first_name.get(),
        'last_name' : last_name.get(),
        'phone' : phone.get(),
        'email' : email.get(),
        'password' : password.get()
    }
    )
    db.commit()  
    sign_up.destroy()  

#........signup page
def sign_up():
	
		
	root.destroy()
	root1=Tk()
	frame1=Frame(root1,padx=100,pady=150,borderwidth=10,bg="black")
	frame1.pack()

	un_label=Label(frame1,text="USERNAME",fg="red",bg="black",font="times 20")
	un_label.grid(row=0,column=0)

	pa_label=Label(frame1,text="PASSWORD",fg="red",bg="black",font="times 20")
	pa_label.grid(row=1,column=0)

	ea_label=Label(frame1,text="EMAIL",fg="red",bg="black",font="times 20")
	ea_label.grid(row=2,column=0)

	cn_label=Label(frame1,text="CONTACT NO.",fg="red",bg="black",font="times 20")
	cn_label.grid(row=3,column=0)

	text_name=StringVar()
	name_e1=Entry(frame1,width=60,textvariable="text_name",borderwidth=5)
	name_e1.grid(row=0,column=1,pady=5)

	text_password=StringVar()
	pass_e1=Entry(frame1,width=60,textvariable="text_password",borderwidth=5)
	pass_e1.grid(row=1,column=1,pady=5)

	text_email=StringVar()
	email_e1=Entry(frame1,width=60,textvariable="text_email",borderwidth=5)
	email_e1.grid(row=2,column=1,padx=10,pady=5)

	text_contact=StringVar()
	con_e1=Entry(frame1,width=60,textvariable="text_contact",borderwidth=5)
	con_e1.grid(row=3,column=1,padx=10,pady=5)



	button4=Button(frame1,text="SIGNUP",padx=20,pady=15,width=20,command=signup_db)
	button4.grid(row=4,column=1,columnspan=2,padx=10,pady=10)
	
	



#......login page
def login():
	def login_db():
		return
	root.destroy()
	root2=Tk()
	frame2=Frame(root2,padx=100,pady=150,borderwidth=10,bg="black")
	frame2.pack()

	un_labe2=Label(frame2,text="USERNAME",fg="red",bg="black",font="times 20")
	un_labe2.grid(row=0,column=0)

	pa_labe2=Label(frame2,text="PASSWORD",fg="red",bg="black",font="times 20")
	pa_labe2.grid(row=1,column=0)

	text_name=StringVar()
	name_e2=Entry(frame2,width=60,textvariable="text_name",borderwidth=5)
	name_e2.grid(row=0,column=1,pady=5)

	text_password=StringVar()
	pass_e2=Entry(frame2,width=60,textvariable="text_password",borderwidth=5)
	pass_e2.grid(row=1,column=1,pady=5)
	


	button5=Button(frame2,text="LOGIN",padx=20,pady=15,width=20,command=login_db)
	button5.grid(row=4,column=1,columnspan=2,padx=10,pady=10)


#.......main body

frame=Frame(root,padx=100,pady=150,borderwidth=10,bg="black")
frame.pack()

lb1=Label(frame,text=" IF NEW USER PLEASE SIGNUP",fg="red",bg="black",font="times 30")
lb1.grid(row=0,column=0,columnspan=3)

button1=Button(frame,text="SIGN-UP",command=sign_up ,width=10)
button1.grid(row=1,column=1)

lb2=Label(frame,text=" IF ACCOUNT EXIST THEN PLEASE LOGIN",fg="red",bg="black",font="times 30",padx=10)
lb2.grid(row=2,column=0,columnspan=3)

button2=Button(frame,text="LOGIN",command=login ,width=10)
button2.grid(row=3,column=1)













root.mainloop()