import tkinter as tk
from tkinter import *
from tkinter import messagebox
from functools import partial
import psycopg2
try:
 conn = psycopg2.connect(database="tkinter_login", user="postgres", password="1234", host="localhost")
 print("connected")
except:
 print ("Unable to connect to the database")
def validateLogin(username,password):
    name=username.get()
    password=password.get()
    if not name:
        messagebox.showerror('Error', 'Please Type username')
    if not password:
        messagebox.showerror('Error', 'Please Type password')
    else:
        cur=conn.cursor()
        cur.execute("Select username,password1 from users where username = %s",(name,))
        row=cur.fetchone()
        if not row:
            messagebox.showerror('Login Status','Username doesn\'t exists')
            return
        if row[0]==name:
            if row[1]==password:
                messagebox.showinfo('Login Status', 'Logged in Successfully!')
                m.destroy()
            else:
                messagebox.showerror('Login Status', 'Incorrect password!')
        else:
            messagebox.showerror('Login Status', 'Incorrect username!')
m=tk.Tk()
m.title('Login')
m.geometry('400x400')
usernameLabel=Label(m,text="User Name").grid(row=0,column=0)
username=StringVar()
usernamefield=Entry(m,textvariable=username).grid(row=0,column=1)
passwordLabel=Label(m,text='Password').grid(row=1,column=0)
password=StringVar()
passwordfield = Entry(m, textvariable=password, show='*').grid(row=1, column=1)
validateLogin=partial(validateLogin,username,password)
button=Button(m,text='Login',command=validateLogin).grid(row=4,column=0)
m.mainloop()

